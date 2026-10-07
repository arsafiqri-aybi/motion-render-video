"""Small explicit models for the included flat-graphics demonstration."""
import math
import numpy as np

def clamp(x, lo=0., hi=1.):
    return max(lo, min(hi, x))

def phase(t, start, duration):
    if duration <= 0:
        raise ValueError('duration must be positive')
    return clamp((t-start)/duration)

def smootherstep(u):
    u=clamp(u)
    return u*u*u*(u*(6*u-15)+10)

def cubic_bezier(points, u):
    p=np.asarray(points, dtype=float)
    if p.shape != (4,2):
        raise ValueError('four 2D control points required')
    v=1-u
    return v**3*p[0]+3*v*v*u*p[1]+3*v*u*u*p[2]+u**3*p[3]

def arc_table(points, samples=1024):
    if samples < 2:
        raise ValueError('at least two intervals required')
    us=np.linspace(0,1,samples+1)
    ps=np.array([cubic_bezier(points,u) for u in us])
    lengths=np.r_[0.,np.cumsum(np.linalg.norm(np.diff(ps,axis=0),axis=1))]
    if lengths[-1] <= 1e-12:
        raise ValueError('degenerate path')
    return us,lengths/lengths[-1],float(lengths[-1])

def arc_point(points, fraction, table):
    us,ss,_=table
    return cubic_bezier(points,float(np.interp(clamp(fraction),ss,us)))

def critical_spring(t, y0=1., v0=0., omega=10.):
    if t < 0 or omega <= 0:
        raise ValueError('nonnegative time and positive omega required')
    b=v0+omega*y0
    e=math.exp(-omega*t)
    return (y0+b*t)*e,(v0-omega*b*t)*e

def pivot_transform(p,c,scale,angle):
    x,y=np.asarray(p)-np.asarray(c)
    cs,sn=math.cos(angle),math.sin(angle)
    return np.asarray(c)+scale*np.array([cs*x-sn*y,sn*x+cs*y])

def source_over(cs, a_s, cb, a_b):
    """RGB inputs are premultiplied, and share an explicitly chosen space."""
    return np.asarray(cs)+np.asarray(cb)*(1-a_s),a_s+a_b*(1-a_s)

def srgb_to_linear(x):
    x=np.asarray(x,dtype=float)
    return np.where(x<=.04045,x/12.92,((x+.055)/1.055)**2.4)

def linear_to_srgb(x):
    x=np.clip(x,0,1)
    return np.where(x<=.0031308,12.92*x,1.055*np.power(x,1/2.4)-.055)

def frame_time(index, rate_num, rate_den=1):
    if index < 0 or rate_num <= 0 or rate_den <= 0:
        raise ValueError('invalid clock')
    return index*rate_den/rate_num

def shutter_samples(t, fps, angle=180., count=4):
    """Forward shutter: [t, t+exposure). Midpoint quadrature, not centered."""
    if count <= 0 or fps <= 0 or not 0 <= angle <= 360:
        raise ValueError('invalid shutter')
    duration=angle/(360*fps)
    return [t+(k+.5)*duration/count for k in range(count)]
