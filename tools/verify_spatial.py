"""Decode and verify the declared silent 3D video, never infer PBR/GPU capability."""
import argparse,hashlib,json,subprocess
from pathlib import Path
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]

def verify(out):
    c=json.loads((ROOT/'examples/spatial.json').read_text());f=out/'spatial.mp4'
    p=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(f)],text=True))
    video=[x for x in p['streams'] if x['codec_type']=='video'];audio=[x for x in p['streams'] if x['codec_type']=='audio']
    assert len(video)==1 and len(audio)==0,'intentional silent example'
    v=video[0];assert (v['width'],v['height'])==(c['width'],c['height'])
    assert int(v['nb_read_frames'])==c['frames']
    assert v['avg_frame_rate']==f"{c['fps_num']}/{c['fps_den']}"
    assert v['pix_fmt']=='yuv420p' and v['color_range']=='tv'
    assert v['color_space']==v['color_transfer']==v['color_primaries']=='bt709'
    assert abs(float(v['duration'])-c['duration_seconds'])<1e-6
    frames=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_frames','-show_entries','frame=best_effort_timestamp_time','-of','json',str(f)],text=True))['frames']
    pts=np.array([float(x['best_effort_timestamp_time']) for x in frames]);expected=np.arange(c['frames'])*c['fps_den']/c['fps_num']
    assert len(pts)==c['frames'] and np.all(np.diff(pts)>0)
    err=float(np.max(abs(pts-expected)));assert err<1e-5
    raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(f),'-f','rawvideo','-pix_fmt','rgb24','-'])
    assert len(raw)==c['frames']*c['width']*c['height']*3
    decoded=np.frombuffer(raw,dtype=np.uint8).reshape(c['frames'],c['height'],c['width'],3)
    # Intended geometry region changes across sequence. Does not certify smoothness.
    difference=float(np.mean(abs(decoded[0,70:310].astype(float)-decoded[-1,70:310].astype(float))))
    assert difference>1,'no observable sequence change'
    for n in [0,19,38,57,76,95]:
        Image.fromarray(decoded[n]).save(out/f'decoded-{n:03d}.png')
    sheet=Image.new('RGB',(c['width']*3,c['height']*2))
    for i,n in enumerate([0,19,38,57,76,95]):sheet.paste(Image.fromarray(decoded[n]),((i%3)*c['width'],(i//3)*c['height']))
    sheet.save(out/'spatial-decoded-contact-sheet.png')
    report={'status':'PASS','video_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'frames':len(pts),'duration_seconds':float(v['duration']),'max_pts_error_seconds':err,'decoded_rgb_bytes':len(raw),'first_last_mean_absolute_difference':difference,'audio_streams':0,'scope':'Actual decoded 3D example: framecount/cadence/duration, SDR tags/range/format, full RGB decode and observable content change. Silent by contract. No GPU/PBR, human comfort or semantic effectiveness certification.'}
    (out/'spatial-media-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report));return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);verify(p.parse_args().out)
