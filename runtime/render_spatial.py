"""Render genuine 3D geometry with an explicitly limited educational CPU pipeline."""
import argparse,hashlib,json,math,subprocess,sys
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFont,__version__ as pillow_version
from motion import phase,smootherstep,linear_to_srgb,shutter_samples
from raster3d import CUBE,FACES,rotate_y,draw_mesh
ROOT=Path(__file__).resolve().parents[1]
C=json.loads((ROOT/'examples/spatial.json').read_text())

def raw_scene(t):
    w,h=C['width'],C['height'];s=C['spatial_samples_per_axis'];w*=s;h*=s;f=C['focal_pixels']*s
    image=np.empty((h,w,3),dtype=np.float64);image[:]=(.78,.75,.68);depth=np.full((h,w),np.inf)
    u=smootherstep(phase(t,.35,2.8));yaw=.50+.65*u
    eye=(7.2*math.sin(yaw),2.8,7.2*math.cos(yaw));target=(0,-.15,0)
    plane=np.array([[-5,-.9,-5],[-5,-.9,5],[5,-.9,5],[5,-.9,-5]])
    draw_mesh(image,depth,plane,[(0,1,2),(0,2,3)],(.57,.56,.49),eye,target,f,C['near'],C['far'])
    # Floor markers are geometry at a distinct height, not a screen-space pasted grid.
    for k in range(-4,5):
        for axis in [0,2]:
            strip=np.array([[k-.012,-.898,-5],[k-.012,-.898,5],[k+.012,-.898,5],[k+.012,-.898,-5]])
            if axis==2:strip=strip[:,[2,1,0]]
            draw_mesh(image,depth,strip,[(0,1,2),(0,2,3)],(.39,.41,.36),eye,target,f,C['near'],C['far'])
    specs=[((0,0,0),.84,-.2+1.25*u,(.63,.14,.055)),((-1.9,-.35,-.6),.53,.16,(.12,.29,.25)),((1.55,-.48,-1.1),.40,-.15,(.75,.66,.44))]
    for pos,size,angle,color in specs:
        points=(CUBE*size)@rotate_y(angle).T+np.array(pos)
        draw_mesh(image,depth,points,FACES,color,eye,target,f,C['near'],C['far'])
    return image,depth

def frame(n,font):
    fps=C['fps_num']/C['fps_den'];t=n/fps;s=C['spatial_samples_per_axis']
    arrays=[raw_scene(tt)[0] for tt in shutter_samples(t,fps,C['shutter_angle'],C['temporal_samples'])]
    rgb=np.mean(arrays,axis=0).reshape(C['height'],s,C['width'],s,3).mean(axis=(1,3))
    im=Image.fromarray(np.rint(linear_to_srgb(rgb)*255).astype(np.uint8));d=ImageDraw.Draw(im)
    d.rectangle((0,0,640,61),fill=(238,233,217))
    d.text((24,12),'RUANG / KAMERA',font=ImageFont.truetype(str(font),22),fill=(26,44,39))
    d.text((24,41),'Geometri 3D - proyeksi - depth buffer',font=ImageFont.truetype(str(font),12),fill=(26,44,39))
    d.rectangle((0,320,640,360),fill=(238,233,217))
    d.text((24,330),'CPU RASTER / 24 FPS / 4 DETIK',font=ImageFont.truetype(str(font),14),fill=(26,44,39))
    return im

def run(out):
    out.mkdir(parents=True,exist_ok=True);frames=out/'frames';frames.mkdir(exist_ok=True)
    family=subprocess.check_output(['fc-match','-f','%{family}',C['font_family']],text=True)
    if C['font_family'] not in family:raise RuntimeError('required font missing')
    font=Path(subprocess.check_output(['fc-match','-f','%{file}',C['font_family']],text=True))
    for p in frames.glob('*.png'):p.unlink()
    for n in range(C['frames']):frame(n,font).save(frames/f'{n:05d}.png')
    vf='format=gbrpf32le,zscale=primariesin=bt709:transferin=iec61966-2-1:matrixin=gbr:rangein=full:primaries=bt709:transfer=bt709:matrix=bt709:range=limited,format=yuv420p'
    subprocess.run(['ffmpeg','-y','-v','error','-framerate',f"{C['fps_num']}/{C['fps_den']}",'-i',str(frames/'%05d.png'),'-vf',vf,'-c:v','libx264','-crf','18','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-an','-movflags','+faststart',str(out/'spatial.mp4')],check=True)
    sheet=Image.new('RGB',(C['width']*3,C['height']*2))
    for i,n in enumerate([0,19,38,57,76,95]):sheet.paste(Image.open(frames/f'{n:05d}.png'),((i%3)*C['width'],(i//3)*C['height']))
    sheet.save(out/'spatial-contact-sheet.png')
    hashfile=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    dependencies=[ROOT/'runtime'/n for n in ['motion.py','raster3d.py','render_spatial.py']]
    report={'status':'RENDER_EXECUTED','config':C,'config_sha256':hashfile(ROOT/'examples/spatial.json'),'code_sha256':{p.name:hashfile(p) for p in dependencies},'video_sha256':hashfile(out/'spatial.mp4'),'font_sha256':hashfile(font),'versions':{'python':sys.version.split()[0],'numpy':np.__version__,'pillow':pillow_version,'ffmpeg':subprocess.check_output(['ffmpeg','-version'],text=True).splitlines()[0]},'scope':'3D opaque geometry; camera transform; six-plane clipping; reciprocal-Z depth; flat authored shading; spatial/temporal sampling; SDR encoding. No Blender, GPU, shadows, GI, PBR, texture interpolation, alpha geometry or audio.'}
    (out/'spatial-render-report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'out':str(out),'frames':C['frames'],'bytes':(out/'spatial.mp4').stat().st_size}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=ROOT/'.local-output/spatial');run(p.parse_args().out.resolve())
