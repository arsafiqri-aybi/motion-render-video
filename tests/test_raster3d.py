"""Independent geometric oracles and visible failure probes for the CPU subset."""
import sys,unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'runtime'))
from raster3d import *

class RasterChecks(unittest.TestCase):
    def test_camera_target_centered(self):
        eye=(3,2,5);target=(.2,-.3,0)
        p=camera_points([target],eye,target)[0]
        np.testing.assert_allclose(p[:2],[0,0],atol=1e-12)
        self.assertAlmostEqual(p[2],np.linalg.norm(np.array(target)-eye))
    def test_camera_up_singularity_fallback(self):
        p=camera_points([(1,1,0)],(0,0,0),(0,1,0))
        self.assertTrue(np.isfinite(p).all())
        with self.assertRaises(ValueError):camera_points([(0,0,0)],(0,0,0),(0,0,0))
    def test_projection_depth_halves_offset(self):
        p=project([[.2,.1,2],[.2,.1,4]],640,360,500)
        np.testing.assert_allclose(p,[[370,155],[345,167.5]])
    def test_near_clip_preserves_halfspace(self):
        p=clip_plane([[0,0,.05],[-1,1,1],[1,1,1]],(0,0,1),-.1)
        self.assertEqual(len(p),4)
        self.assertTrue(np.all(p[:,2]>=.1-1e-12))
        self.assertEqual(sum(abs(p[:,2]-.1)<1e-10),2)
    def test_fully_clipped_and_far_rejection(self):
        for z in [.05,110]:
            p=clip_frustum([[0,0,z],[1,0,z],[0,1,z]],640,360,410)
            self.assertEqual(len(p),0)
    def test_frustum_bounds_after_clipping(self):
        p=clip_frustum([[-10,-10,2],[10,-10,2],[0,10,2]],64,64,32)
        xy=project(p,64,64,32)
        self.assertTrue((xy>=-1e-9).all() and (xy<=64+1e-9).all())
    def test_depth_matches_ray_plane_oracle(self):
        # Plane z-x=3; ray through pixel center has x/z=.5/32.
        im=np.zeros((64,64,3));dep=np.full((64,64),np.inf)
        v=[[-1,-1,2],[1,-1,4],[0,1,3]]
        triangle(im,dep,v,(1,0,0),32)
        expected=3/(1-.5/32)
        self.assertAlmostEqual(dep[32,32],expected,places=12)
    def test_opaque_occlusion_order_independent(self):
        far=np.array([[-1,-1,4],[1,-1,4],[0,1,4]],float)
        near=far.copy();near[:,:2]*=.5;near[:,2]=2
        images=[]
        for order in [[(far,(0,0,1)),(near,(1,0,0))],[(near,(1,0,0)),(far,(0,0,1))]]:
            im=np.zeros((64,64,3));dep=np.full((64,64),np.inf)
            for v,col in order:triangle(im,dep,v,col,32)
            images.append(im)
        np.testing.assert_array_equal(*images)
        np.testing.assert_array_equal(images[0][32,32],[1,0,0])
    def test_degenerate_triangle_no_write(self):
        im=np.zeros((16,16,3));dep=np.full((16,16),np.inf)
        triangle(im,dep,[[0,0,2],[1,1,2],[2,2,2]],(1,1,1),8)
        self.assertEqual(np.count_nonzero(im),0)
    def test_shared_edge_no_holes(self):
        im=np.zeros((32,32,3));dep=np.full((32,32),np.inf)
        v=np.array([[-1,-1,2],[1,-1,2],[1,1,2],[-1,1,2]],float)
        for ids in [[0,1,2],[0,2,3]]:triangle(im,dep,v[ids],(1,1,1),16)
        self.assertTrue(np.all(im[8:24,8:24]==1))
    def test_normal_inverse_transpose_orthogonal(self):
        a=np.diag([2.,1.,3.]);n=unit([1,1,0]);t=np.array([1,-1,0.])
        nt=normal_transform(n,a)
        self.assertAlmostEqual(float(np.dot(nt,a@t)),0,places=12)
        self.assertAlmostEqual(np.linalg.norm(nt),1,places=12)
    def test_dolly_zoom_subject_scale_invariant(self):
        sizes=[]
        for distance,f in [(10,50),(20,100)]:
            ps=project([[-1,0,distance],[1,0,distance]],640,360,f)
            sizes.append(ps[1,0]-ps[0,0])
        self.assertEqual(sizes,[10,10])

if __name__=='__main__':unittest.main()
