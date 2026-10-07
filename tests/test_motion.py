import sys,math,unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'runtime'))
from motion import *

class MotionChecks(unittest.TestCase):
    def test_spring_initial_conditions(self):
        self.assertEqual(critical_spring(0,2,3),(2,3))
    def test_spring_known_value(self):
        y,v=critical_spring(.5)
        self.assertAlmostEqual(y,6*math.exp(-5),places=12)
        self.assertAlmostEqual(v,-50*math.exp(-5),places=12)
    def test_spring_independent_ode_residual(self):
        # Finite difference derivative of velocity checks equation, not copied closed form.
        t=.37;h=1e-5;w=8
        y,v=critical_spring(t,1,.4,w)
        acceleration=(critical_spring(t+h,1,.4,w)[1]-critical_spring(t-h,1,.4,w)[1])/(2*h)
        self.assertLess(abs(acceleration+2*w*v+w*w*y),1e-6)
    def test_arc_length_exact_reference(self):
        _,_,length=arc_table([(0,0),(0,1),(1,1),(1,0)],4096)
        # Speed=3*(2u²-2u+1) integrates to exactly2 on[0,1].
        self.assertLess(abs(length-2),1e-7)
    def test_arc_inversion_equal_distances(self):
        points=[(0,0),(0,1),(1,1),(1,0)];table=arc_table(points)
        ps=np.array([arc_point(points,k/200,table) for k in range(201)])
        lengths=np.linalg.norm(np.diff(ps,axis=0),axis=1)
        self.assertLess(float(np.max(lengths)-np.min(lengths)),1e-5)
    def test_pivot_invariant(self):
        np.testing.assert_allclose(pivot_transform([5,9],[5,9],3,1.2),[5,9])
    def test_source_over_oracle_and_noncommutativity(self):
        rgb,a=source_over([.5,0,0],.5,[0,0,1],1)
        np.testing.assert_allclose(rgb,[.5,0,.5]);self.assertEqual(a,1)
        reversed_rgb,_=source_over([0,0,1],1,[.5,0,0],.5)
        self.assertFalse(np.allclose(rgb,reversed_rgb))
    def test_linear_light_midpoint(self):
        self.assertAlmostEqual(float(linear_to_srgb(np.array(.5))),.7353569830524495,places=12)
        values=np.linspace(0,1,101)
        np.testing.assert_allclose(linear_to_srgb(srgb_to_linear(values)),values,atol=1e-14)
    def test_exact_clock(self):
        self.assertAlmostEqual(frame_time(180,30000,1001),6.006)
        self.assertAlmostEqual(frame_time(179,30),5.966666666666667)
    def test_forward_shutter_footprint(self):
        ts=shutter_samples(1,30,180,4)
        self.assertTrue(all(1<t<1+1/60 for t in ts))
        self.assertAlmostEqual(sum(ts)/4,1+1/120)
    def test_phase_boundaries(self):
        self.assertEqual(phase(-1,0,1),0);self.assertEqual(phase(2,0,1),1)
        self.assertAlmostEqual(smootherstep(.5),.5)
        with self.assertRaises(ValueError):phase(0,0,0)
    def test_invalid_degenerate_path(self):
        with self.assertRaises(ValueError):arc_table([(0,0)]*4)

if __name__=='__main__':unittest.main()
