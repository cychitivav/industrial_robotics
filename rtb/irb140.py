import roboticstoolbox as rtb  # Robotics and numerical libraries
from spatialmath import *
from spatialmath.base import *
import numpy as np
import matplotlib.pyplot as plt


class irb140(rtb.DHRobot):
    def __init__(self):
        self.L = [rtb.DHLink(d=0.352, a=0.07, alpha=-np.pi/2),
                  rtb.DHLink(d=0,     a=0.36, alpha=0, offset=-np.pi/2),
                  rtb.DHLink(d=0,     a=0,    alpha=-np.pi/2),
                  rtb.DHLink(d=0.38,  a=0,    alpha=np.pi/2),
                  rtb.DHLink(d=0,     a=0,    alpha=-np.pi/2),
                  rtb.DHLink(d=0.065, a=0,    alpha=0)]

        super().__init__(
            self.L,
            name="irb140"
        )
        # ,
        #     tool=SE3(trnorm(transl([0.012254, -0.000002, 0.214736])
        #              @ r2t(q2r(([0.923879533, 0, 0.382683432, 0])))))

    def MoveJ(self, T0, Tf, n):
        q0 = self.ikine(T0)
        qf = self.ikine(Tf)

        return rtb.jtraj(q0, qf, n).q

    def MoveL(self, T0, Tf, n):
        Hs = rtb.ctraj(T0, Tf, n)

        q = np.ndarray((n, 6))

        for i, H in enumerate(Hs):
            q[i, :] = self.ikine(H)

        return q

    def MoveC(self, T0, Tc, Tf, n):
        # self.fkine_path(q)
        return self.MoveJ(T0, Tf, n)

    def ikine(self, T, config='uf'):
        q = np.zeros(6)

        w = T.t - self.d[5]*T.a
        w = np.append(w,1)

        q[0] = np.arctan2(w[1],w[0])

        w1 = np.linalg.inv(self.A(0,q))@w

        r = np.sqrt(w1[0]**2+w1[1]**2)
        gamma = np.arccos((self.d[3]**2-self.a[1]**2-r**2)/(-2*r*self.a[1]))
        beta = np.arctan2(-w1[1],w1[0])

        if 'u' in config:
            q[1] = np.pi/2-gamma-beta
        elif 'd' in config:
            q[1] = np.pi/2+gamma-beta
        else:
            raise ValueError("config must contain 'u' or 'd'")
        

        eta = np.arccos((r**2-self.a[1]**2-self.d[3]**2)/(-2*self.a[1]*self.d[3]))

        if 'u' in config:
            q[2] = np.pi/2-eta
        elif 'd' in config:
            q[2] = eta-3*np.pi/2

        R36 = self.A(2,q).R.T@T.R

        q[3] = np.arctan2(R36[1,2],R36[0,2])+np.pi
        q[4] = np.arccos(R36[2,2])
        q[5] = np.arctan2(R36[2,1],-R36[2,0])+np.pi

        return q


if __name__ == "__main__":
    irb140 = irb140()
    print(irb140)

    Home = irb140.fkine([0, 0, 0, 0, 0, 0])
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
    qs = np.vstack((irb140.MoveL(Home, wobj*P5, n),  # Brayan
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

    points = irb140.fkine(qs).t
    print(points)

    q1 = [0,0,0,0,0,0]

    # qs = np.array([q1,irb140.ikine(irb140.fkine(q1),config="uf")])
    # print(qs)

    # irb140.teach()

    irb140.plot(qs, dt=0.1, jointaxes=True)#, movie='BJC.gif')
    plt.plot(points[:,0], points[:,1], points[:,2])
    # trplot(Home.A, frame='A', style="rviz", width=1, length=0.2)
    input()
