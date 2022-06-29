import roboticstoolbox as rtb  # Robotics and numerical libraries
from spatialmath import *
from spatialmath.base import *
import numpy as np

if __name__ == "__main__":
    irb140 = rtb.DHRobot(
        [rtb.DHLink(d=0.352, a=0.07, alpha=-np.pi/2),
         rtb.DHLink(d=0,     a=0.36, alpha=0, offset=-np.pi/2),
         rtb.DHLink(d=0,     a=0,    alpha=-np.pi/2),
         rtb.DHLink(d=0.38,  a=0,    alpha=np.pi/2),
         rtb.DHLink(d=0,     a=0,    alpha=-np.pi/2),
         rtb.DHLink(d=0.065, a=0,    alpha=0)],
        name="irb140",
        tool=transl([0.012254,-0.000002,0.214736])@r2t(q2r(([0.923879533,0,0.382683432,0])))
    )

    Home = transl([506.292,0,679.5])*r2t(q2r([0.5,0,0.866025404,0]))
    
    # Brayan points
    P1 = transl([35,135,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P2 = transl([35,85,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P3 = transl([35,25,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P4 = transl([60,25,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P5 = transl([55,85,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P6 = transl([75,115,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P7 = transl([85,60,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    
    P7u = transl([85,60,30])@r2t(q2r([0,0.707106781,0.707106781,0])) 
    
    # Julian points
    P8 = transl([100,135,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P9 = transl([145,135,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P10 = transl([145,50,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P11 = transl([125,25,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P12 = transl([100,50,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    
    P12u = transl([100,50,30])@r2t(q2r([0,0.707106781,0.707106781,0]))
    
    # Cristian points
    P13 = transl([220,110,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P14 = transl([225,125,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P15 = transl([210,133,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P16 = transl([180,120,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P17 = transl([162,40,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P18 = transl([190,25,0])@r2t(q2r([0,0.707106781,0.707106781,0]))
    P19 = transl([210,50,0])@r2t(q2r([0,0.707106781,0.707106781,0]))

    irb140.plot([0, 0, 0, 0, 0, 0])
    input()

