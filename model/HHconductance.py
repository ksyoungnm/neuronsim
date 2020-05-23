# File: conductance.py
'''
Contains the original HH equations. Parameters were taken
from

Johnston, D., & Wu, S. M. (1995). Foundations of cellular neurophysiology.
MIT Press.

Method of integrating is slightly different from the classes
found in the conductance.py model, so the behavior is a little strange.
To produce action potentials, hold at -0.5 nA or so, then jump up to
5 nA. The sudden increase causes action potentials, but if the movement up
is too slow the neuron won't fire. This needs a little more cleaning up.
'''
import math

class Conductance:

    def __init__(self, gbar, e_rev):
        self.gbar = gbar
        self.e_rev = e_rev
        self.g = 0.0
                
    def get_g(self):
        return self.g

    def get_ge(self):
        return self.g*self.e_rev

    def integrate(self, v, dt):
        raise Exception("Overwrite this.")

class HHNa(Conductance):

    def __init__(self, gbar=95.0174, e_rev=60):
        super().__init__(gbar, e_rev)
        self.m = 0.0
        self.h = 0.0

    def integrate(self, v, dt):
        tau_m = 1/(self.alpha_m(v)+self.beta_m(v))
        m_inf = tau_m*self.alpha_m(v)

        tau_h = 1/(self.alpha_h(v)+self.beta_h(v))
        h_inf = tau_h*self.alpha_h(v)

        m = m_inf + (self.m - m_inf)*math.exp(-dt/tau_m)
        h = h_inf + (self.h - h_inf)*math.exp(-dt/tau_h)

        self.g = self.gbar*m*m*m*h

        self.m = m
        self.h = h

    def alpha_m(self, v):
        return (0.1*(-v+25))/(math.exp((-v+25)/10)-1)
    
    def beta_m(self, v):
        return 4*math.exp(-v/18)
    
    def alpha_h(self, v):
        return 0.07*math.exp(-v/20)
    
    def beta_h(self, v):
        return 1/(math.exp((-v+30)/10)+1)


class HHK(Conductance):

    def __init__(self, gbar=18.0006, e_rev=-90):
        super().__init__(gbar, e_rev)
        self.n = 0.0

    def integrate(self, v, dt):
        tau_n = 1/(self.alpha_n(v)+self.beta_n(v))
        n_inf = tau_n*self.alpha_n(v)

        n = n_inf + (self.n - n_inf)*math.exp(-dt/tau_n)
        
        self.g = self.gbar*n*n*n*n

        self.n = n

    def alpha_n(self, v):
        return (0.01*(-v+10))/(math.exp((-v+10)/10)-1)
    
    def beta_n(self, v):
        return 0.125*math.exp(-v/80)
