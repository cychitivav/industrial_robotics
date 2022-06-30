import roboticstoolbox as rtb  # Robotics and numerical libraries
from spatialmath import *
from spatialmath.base import *
import numpy as np


class irb140(rtb.DHRobot):
    def __init__(self):
        super().__init__(
            [rtb.DHLink(d=0.352, a=0.07, alpha=-np.pi/2),
             rtb.DHLink(d=0,     a=0.36, alpha=0, offset=-np.pi/2),
             rtb.DHLink(d=0,     a=0,    alpha=-np.pi/2),
             rtb.DHLink(d=0.38,  a=0,    alpha=np.pi/2),
             rtb.DHLink(d=0,     a=0,    alpha=-np.pi/2),
             rtb.DHLink(d=0.065, a=0,    alpha=0)],
            name="irb140",
            tool=SE3(trnorm(transl([0.012254, -0.000002, 0.214736])
                     @ r2t(q2r(([0.923879533, 0, 0.382683432, 0])))))
        )

    def MoveJ(self, T0, Tf, n):
        q0 = self.ikine_min(T0).q
        qf = self.ikine_min(Tf).q

        return rtb.jtraj(q0, qf, n).q

    def MoveL(self, T0, Tf, n):
        Hs = rtb.ctraj(T0, Tf, n)

        q = np.ndarray((n, 6))

        for i, H in enumerate(Hs):
            q[i, :] = self.ikine_min(H).q

        return q

    def MoveC(self, T0, Tc, Tf, n):
        return self.MoveJ(T0, Tf, n)


if __name__ == "__main__":
    irb140 = irb140()

    Home = irb140.fkine([0,0,0,0,0,0])
    wobj = SE3(trnorm(transl([0.653753, 0.399386, 0.025]) @
               r2t(q2r([0.363649594, 0, 0, 0.931535814]))))

    # Brayan points
    P1 = SE3(trnorm(transl([0.035, 0.135, 0]) @
             r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P2 = SE3(trnorm(transl([0.035, 0.085, 0]) @
             r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P3 = SE3(trnorm(transl([0.035, 0.025, 0]) @
             r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P4 = SE3(trnorm(transl([0.060, 0.025, 0]) @
             r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P5 = SE3(trnorm(transl([0.055, 0.085, 0]) @
             r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P6 = SE3(trnorm(transl([0.075, 0.115, 0]) @
             r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P7 = SE3(trnorm(transl([0.085, 0.060, 0]) @
             r2t(q2r([0, 0.707106781, 0.707106781, 0]))))

    P7u = SE3(trnorm(transl([0.085, 0.060, 0.030]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))

    # Julian points
    P8 = SE3(trnorm(transl([0.100, 0.135, 0]) @
             r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P9 = SE3(trnorm(transl([0.145, 0.135, 0]) @
             r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P10 = SE3(trnorm(transl([0.145, 0.050, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P11 = SE3(trnorm(transl([0.125, 0.025, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P12 = SE3(trnorm(transl([0.100, 0.050, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))

    P12u = SE3(trnorm(transl([0.100, 0.050, 0.030]) @
               r2t(q2r([0, 0.707106781, 0.707106781, 0]))))

    # Cristian points
    P13 = SE3(trnorm(transl([0.220, 0.110, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P14 = SE3(trnorm(transl([0.225, 0.125, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P15 = SE3(trnorm(transl([0.210, 0.133, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P16 = SE3(trnorm(transl([0.180, 0.120, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P17 = SE3(trnorm(transl([0.162, 0.040, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P18 = SE3(trnorm(transl([0.190, 0.025, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))
    P19 = SE3(trnorm(transl([0.210, 0.050, 0]) @
              r2t(q2r([0, 0.707106781, 0.707106781, 0]))))

    # Path planning
    n = 4
    qs = np.vstack((irb140.MoveJ(Home, wobj*P5, n),  # Brayan
                    irb140.MoveL(wobj*P5, wobj*P2, n),
                    irb140.MoveL(wobj*P2, wobj*P1, n),
                    irb140.MoveC(wobj*P1, wobj*P6, wobj*P5, n),
                    irb140.MoveC(wobj*P5, wobj*P7, wobj*P4, n),
                    irb140.MoveL(wobj*P4, wobj*P3, n),
                    irb140.MoveL(wobj*P3, wobj*P2, n),
                    irb140.MoveL(wobj*P2, wobj*P7u, n),
                    irb140.MoveJ(wobj*P7u, wobj*P8, n),  # Julian
                    irb140.MoveL(wobj*P8, wobj*P9, n),
                    irb140.MoveL(wobj*P9, wobj*P10, n),
                    irb140.MoveC(wobj*P10, wobj*P11, wobj*P12, n),
                    irb140.MoveL(wobj*P12, wobj*P12u, n),
                    irb140.MoveJ(wobj*P12u, wobj*P13, n),  # Cristian
                    irb140.MoveC(wobj*P13, wobj*P14, wobj*P15, n),
                    irb140.MoveC(wobj*P15, wobj*P16, wobj*P17, n),
                    irb140.MoveC(wobj*P17, wobj*P18, wobj*P19, n),
                    irb140.MoveJ(wobj*P19, Home, n)))

    irb140.plot(qs, dt=1, jointaxes=True,movie='BJC.gif')
    input()
