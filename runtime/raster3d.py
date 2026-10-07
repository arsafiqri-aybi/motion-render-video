"""Educational CPU 3D rasterizer: positive camera Z, flat shading, opaque triangles."""
import math
import numpy as np

def unit(v):
    v=np.asarray(v,dtype=float);n=np.linalg.norm(v)
    if n<1e-12:raise ValueError('zero vector')
    return v/n

def camera_points(points,eye,target,up=(0,1,0)):
    eye=np.asarray(eye,dtype=float);forward=unit(np.asarray(target)-eye)
    if abs(float(np.dot(forward,unit(up))))>.999:
        up=(1,0,0) if abs(forward[0])<.9 else (0,0,1)
    right=unit(np.cross(forward,up));true_up=unit(np.cross(right,forward))
    return (np.asarray(points)-eye)@np.column_stack((right,true_up,forward))

def rotate_y(angle):
    c,s=math.cos(angle),math.sin(angle)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]],dtype=float)

def normal_transform(n,linear):
    return unit(np.linalg.inv(linear).T@np.asarray(n,dtype=float))

def project(points,width,height,focal):
    p=np.asarray(points,dtype=float)
    if np.any(p[:,2]<=0):raise ValueError('clip before projecting nonpositive depth')
    return np.column_stack((width/2+focal*p[:,0]/p[:,2],height/2-focal*p[:,1]/p[:,2]))

def clip_plane(vertices,normal,offset):
    """Sutherland-Hodgman for dot(normal,p)+offset>=0 in camera space."""
    poly=[np.asarray(v,dtype=float) for v in vertices];out=[]
    if not poly:return np.empty((0,3))
    for i,b in enumerate(poly):
        a=poly[i-1];da=float(np.dot(normal,a)+offset);db=float(np.dot(normal,b)+offset)
        ina,inb=da>=0,db>=0
        if ina!=inb:out.append(a+(b-a)*(da/(da-db)))
        if inb:out.append(b)
    return np.array(out).reshape((-1,3))

def clip_frustum(vertices,width,height,focal,near=.1,far=100.):
    if not 0<near<far or focal<=0:raise ValueError('invalid frustum')
    p=np.asarray(vertices,dtype=float)
    ax,ay=width/(2*focal),height/(2*focal)
    planes=[((0,0,1),-near),((0,0,-1),far),((1,0,ax),0),((-1,0,ax),0),((0,1,ay),0),((0,-1,ay),0)]
    for n,d in planes:
        p=clip_plane(p,np.asarray(n),d)
        if not len(p):break
    return p

def triangle(image,depth,vertices,color,focal):
    """Rasterize an already-clipped triangle at pixel centers; reciprocal Z interpolation."""
    h,w=depth.shape;v=np.asarray(vertices,dtype=float);xy=project(v,w,h,focal)
    x0,y0=xy[0];x1,y1=xy[1];x2,y2=xy[2]
    den=(y1-y2)*(x0-x2)+(x2-x1)*(y0-y2)
    if abs(den)<1e-12:return
    lo=np.maximum(0,np.floor(xy.min(axis=0)).astype(int));hi=np.minimum([w-1,h-1],np.ceil(xy.max(axis=0)).astype(int))
    if np.any(lo>hi):return
    xx,yy=np.meshgrid(np.arange(lo[0],hi[0]+1)+.5,np.arange(lo[1],hi[1]+1)+.5)
    a=((y1-y2)*(xx-x2)+(x2-x1)*(yy-y2))/den
    b=((y2-y0)*(xx-x2)+(x0-x2)*(yy-y2))/den;c=1-a-b
    inside=(a>=-1e-10)&(b>=-1e-10)&(c>=-1e-10)
    inv=a/v[0,2]+b/v[1,2]+c/v[2,2]
    z=np.full(inv.shape,np.inf);np.divide(1,inv,out=z,where=inv>0)
    db=depth[lo[1]:hi[1]+1,lo[0]:hi[0]+1];ib=image[lo[1]:hi[1]+1,lo[0]:hi[0]+1]
    mask=inside&(z<db-1e-10);db[mask]=z[mask];ib[mask]=color

def draw_mesh(image,depth,points,faces,base,eye,target,focal,near=.1,far=100.,light=(-.5,1,.8)):
    points=np.asarray(points);cam=camera_points(points,eye,target);light=unit(light)
    for face in faces:
        q=points[list(face)];n=unit(np.cross(q[1]-q[0],q[2]-q[0]))
        color=np.asarray(base)*(.22+.78*max(0,float(np.dot(n,light))))
        clipped=clip_frustum(cam[list(face)],image.shape[1],image.shape[0],focal,near,far)
        for i in range(1,len(clipped)-1):triangle(image,depth,clipped[[0,i,i+1]],color,focal)

CUBE=np.array([[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]],dtype=float)
FACES=[(0,3,2),(0,2,1),(4,5,6),(4,6,7),(1,2,6),(1,6,5),(0,4,7),(0,7,3),(3,7,6),(3,6,2),(0,1,5),(0,5,4)]
