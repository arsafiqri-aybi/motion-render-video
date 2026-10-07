"""Render an original, deterministic six-second flat motion graphic."""
import argparse,hashlib,json,math,subprocess,sys,wave
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFont,__version__ as pillow_version
from motion import phase,smootherstep,arc_table,arc_point,srgb_to_linear,linear_to_srgb,shutter_samples
ROOT=Path(__file__).resolve().parents[1]
C=json.loads((ROOT/'examples/demo.json').read_text())
W,H=C['width'],C['height']
S=2  # spatial coverage approximation, then Lanczos downsample
PATH=[(96,218),(175,78),(430,310),(544,168)]
TABLE=arc_table(PATH)

def font_file():
    p=Path(subprocess.check_output(['fc-match','-f','%{file}',C['font_family']],text=True).strip())
    if not p.is_file():
        raise RuntimeError('install DejaVu Sans or configure an explicit font')
    # No silent family substitution: verify the requested family is present.
    family=subprocess.check_output(['fc-match','-f','%{family}',C['font_family']],text=True)
    if C['font_family'] not in family:
        raise RuntimeError('required font family unavailable')
    return p
FONT=None

def scene(t):
    im=Image.new('RGB',(W*S,H*S),(242,236,222));d=ImageDraw.Draw(im)
    def line(ps,fill,width=1):d.line([(int(x*S),int(y*S)) for x,y in ps],fill=fill,width=width*S)
    def text(x,y,s,size,fill=(29,47,45)):
        d.text((x*S,y*S),s,font=ImageFont.truetype(str(FONT),size*S),fill=fill)
    def circle(x,y,r,fill):d.ellipse(((x-r)*S,(y-r)*S,(x+r)*S,(y+r)*S),fill=fill)
    ink=(29,47,45);accent=(192,73,42);muted=(166,171,152)
    text(32,22,'MOTION / RENDER / VIDEO',16)
    text(32,50,'Gerak menjadi tampilan.',28)
    line([(32,103),(608,103)],muted)
    points=[tuple(arc_point(PATH,k/120,TABLE)) for k in range(121)]
    line(points,(208,203,188),2)
    u=smootherstep(phase(t,.5,1.5))
    p=arc_point(PATH,u,TABLE)
    # Morph radial profile: circle -> rounded-square-like superellipse.
    morph=smootherstep(phase(t,2.,1.5));exponent=2+4*morph
    rot=.3*math.sin(math.pi*morph)
    poly=[]
    for a in np.linspace(0,2*math.pi,96,endpoint=False):
        x=25*math.copysign(abs(math.cos(a))**(2/exponent),math.cos(a))
        y=25*math.copysign(abs(math.sin(a))**(2/exponent),math.sin(a))
        poly.append(((p[0]+x*math.cos(rot)-y*math.sin(rot))*S,(p[1]+x*math.sin(rot)+y*math.cos(rot))*S))
    d.polygon(poly,fill=accent)
    # Fixed anchor marks make the motion legible without adding competing motion.
    circle(96,218,4,ink);circle(544,168,4,ink)
    # Three authored stages, staggered without moving text during reading holds.
    for i,(label,cue) in enumerate([('BENTUK',.5),('WAKTU',2.),('SUARA',3.5)]):
        reveal=smootherstep(phase(t,cue,.35));x=32+i*202
        col=tuple(round((242,236,222)[j]+(ink[j]-(242,236,222)[j])*reveal) for j in range(3))
        text(x,275,label,15,col)
        if reveal > 0: line([(x,306),(x+int(160*reveal),306)],accent,3)
    # A small audiovisual accent ring at each specified cue, continuous envelope.
    for cue in C['cues']:
        age=t-cue
        if 0<=age<.3:
            q=age/.3;r=29+18*q
            col=tuple(round(accent[j]*(1-q)+(242,236,222)[j]*q) for j in range(3))
            d.ellipse(((p[0]-r)*S,(p[1]-r)*S,(p[0]+r)*S,(p[1]+r)*S),outline=col,width=2*S)
    progress=max(0,min(1,t/C['duration']))
    line([(32,337),(32+int(576*progress),337)],ink,2)
    return im.resize((W,H),Image.Resampling.LANCZOS)

def frame(n):
    fps=C['fps_num']/C['fps_den'];t=n/fps
    samples=shutter_samples(t,fps,C['shutter_angle'],C['temporal_samples'])
    rgb=[np.asarray(scene(tt),dtype=np.float64)/255 for tt in samples]
    mean=np.mean([srgb_to_linear(a) for a in rgb],axis=0)
    return Image.fromarray(np.rint(linear_to_srgb(mean)*255).astype(np.uint8))

def audio(out):
    fs=C['sample_rate'];n=round(C['duration']*fs);signal=np.zeros(n)
    for j,cue in enumerate(C['cues']):
        start=round(cue*fs);length=round(.18*fs);ts=np.arange(length)/fs
        envelope=np.sin(np.pi*np.arange(length)/length)**2*np.exp(-18*ts)
        signal[start:start+length]+=.35*envelope*np.sin(2*np.pi*(330+110*j)*ts)
    pcm=np.rint(np.clip(signal,-1,1)*32767).astype('<i2')
    with wave.open(str(out),'wb') as f:
        f.setnchannels(1);f.setsampwidth(2);f.setframerate(fs);f.writeframes(pcm.tobytes())
    return {'samples':n,'sample_peak':float(np.max(np.abs(signal))),'cues_seconds':C['cues']}

def run(out):
    global FONT
    FONT=font_file();out.mkdir(parents=True,exist_ok=True);frames=out/'frames';frames.mkdir(exist_ok=True)
    count=round(C['duration']*C['fps_num']/C['fps_den'])
    # Remove only frame outputs from this explicitly selected output directory.
    for p in frames.glob('*.png'):p.unlink()
    for n in range(count):
        frame(n).save(frames/f'{n:05d}.png')
    ar=audio(out/'audio.wav')
    vf='format=gbrpf32le,zscale=primariesin=bt709:transferin=iec61966-2-1:matrixin=gbr:rangein=full:primaries=bt709:transfer=bt709:matrix=bt709:range=limited,format=yuv420p'
    command=['ffmpeg','-y','-hide_banner','-loglevel','error','-framerate',f"{C['fps_num']}/{C['fps_den']}",'-i',str(frames/'%05d.png'),'-i',str(out/'audio.wav'),'-vf',vf,'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-c:a','aac','-b:a','128k','-movflags','+faststart',str(out/'demo.mp4')]
    subprocess.run(command,check=True)
    sheet=Image.new('RGB',(W*3,H*2))
    for i,n in enumerate([0,30,60,90,120,179]):
        sheet.paste(Image.open(frames/f'{n:05d}.png'),((i%3)*W,(i//3)*H))
    sheet.save(out/'contact-sheet.png')
    h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    report={'config':C,'frame_count':count,'audio_source':ar,'font':{'name':FONT.name,'sha256':h(FONT)},'versions':{'python':sys.version.split()[0],'numpy':np.__version__,'pillow':pillow_version,'ffmpeg':subprocess.check_output(['ffmpeg','-version'],text=True).splitlines()[0]},'config_sha256':h(ROOT/'examples/demo.json'),'code_sha256':{p.name:h(p) for p in (ROOT/'runtime').glob('*.py')},'mp4_sha256':h(out/'demo.mp4'),'scope':'Executed flat 2D demo; not a GPU/3D, HDR, complex script shaping, human comprehension or accessibility certification.'}
    (out/'render-report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'out':str(out),'frames':count,'bytes':(out/'demo.mp4').stat().st_size}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=ROOT/'.local-output')
    run(parser.parse_args().out.resolve())
