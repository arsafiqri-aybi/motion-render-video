"""Verify actual decoded media properties. No claims about all human perception."""
import argparse,hashlib,json,subprocess,wave
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def probe(path,args):
    return json.loads(subprocess.check_output(['ffprobe','-v','error',*args,'-of','json',str(path)],text=True))

def verify(out):
    cfg=json.loads((ROOT/'examples/demo.json').read_text());file=out/'demo.mp4'
    data=probe(file,['-count_frames','-show_streams','-show_format'])
    vs=[s for s in data['streams'] if s['codec_type']=='video'];aus=[s for s in data['streams'] if s['codec_type']=='audio']
    assert len(vs)==len(aus)==1,'one video and one audio stream required'
    v,a=vs[0],aus[0];fps=cfg['fps_num']/cfg['fps_den'];count=round(cfg['duration']*fps)
    assert (v['width'],v['height'])==(cfg['width'],cfg['height'])
    assert int(v['nb_read_frames'])==count
    assert v['avg_frame_rate']==f"{cfg['fps_num']}/{cfg['fps_den']}"
    assert v['pix_fmt']=='yuv420p'
    assert v['color_space']==v['color_transfer']==v['color_primaries']=='bt709'
    assert v['color_range']=='tv'
    assert int(a['sample_rate'])==cfg['sample_rate'] and a['channels']==1
    assert abs(float(v['duration'])-cfg['duration'])<1e-5
    assert abs(float(data['format']['duration'])-cfg['duration'])<1/fps
    decoded=probe(file,['-select_streams','v:0','-show_frames','-show_entries','frame=best_effort_timestamp_time'])
    pts=np.array([float(f['best_effort_timestamp_time']) for f in decoded['frames']])
    assert len(pts)==count and np.all(np.diff(pts)>0)
    cadence_error=float(np.max(np.abs(pts-np.arange(count)/fps)))
    assert cadence_error<1e-5
    subprocess.run(['ffmpeg','-v','error','-i',str(file),'-f','null','-'],check=True)
    raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(file),'-map','0:a:0','-f','f32le','-ac','1','-ar',str(cfg['sample_rate']),'-'])
    pcm=np.frombuffer(raw,dtype='<f4');fs=cfg['sample_rate']
    assert np.isfinite(pcm).all() and np.max(np.abs(pcm))<1
    window=round(.005*fs)
    rms=np.array([np.sqrt(np.mean(pcm[i:i+window]**2)) for i in range(0,len(pcm)-window+1,window)])
    cues=[]
    for cue in cfg['cues']:
        # Envelope onset may follow mathematical cue; threshold/window define observation.
        lo=max(0,int((cue-.03)/.005));hi=int((cue+.08)/.005)
        crossings=np.flatnonzero(rms[lo:hi]>.001)
        assert len(crossings),'cue missing'
        onset=(lo+int(crossings[0]))*.005;offset=onset-cue
        assert -.015<=offset<=.035,('onset outside declared tolerance',cue,offset)
        cues.append({'cue_seconds':cue,'detected_window_start_seconds':onset,'offset_seconds':round(offset,6)})
    assert abs(len(pcm)/fs-cfg['duration'])<.03 # AAC decoded padding can remain.
    report={'status':'PASS','scope':'Decoded dimensions, CFR cadence/count, video/container duration, BT709 tags/range/pixel format, audio rate/channels, full decode, finite audio/headroom and four threshold-defined cue onsets. Not a comprehension, accessibility, loudness compliance or color calibration certification.','sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'frames':len(pts),'duration_seconds':float(data['format']['duration']),'max_pts_error_seconds':cadence_error,'audio_decoded_samples':len(pcm),'audio_decoded_peak':float(np.max(np.abs(pcm))),'cue_measurement':{'method':'5ms RMS windows; first RMS >0.001 within cue -30ms/+80ms','tolerance_seconds':[-.015,.035],'events':cues},'video_stream':{k:v.get(k) for k in ['codec_name','width','height','pix_fmt','avg_frame_rate','color_range','color_space','color_transfer','color_primaries']}}
    (out/'media-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);verify(p.parse_args().out)
