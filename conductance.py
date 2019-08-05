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
        raise Exception("this method needs to be overwritten")


class NaV(Conductance):

    def __init__(self, gbar=95.0174, e_rev=60):
        Conductance.__init__(self, gbar, e_rev)
        self.m = 0.0
        self.h = 0.0

    def integrate(self, v, dt):
        m_inf = 1/(1+math.exp((v+25.5)/-5.29))
        tau_m = 1.32 - (1.26/(1+math.exp((v+120)/-25)))
    
        h_inf = 1/(1+math.exp((v+48.9)/5.18))
        tau_h = (0.67/(1+math.exp((v+62.9)/-10)))*(1.5 + (1/(1+math.exp((v+34.9)/3.6))))
    
        m = m_inf + (self.m - m_inf)*math.exp(-dt/tau_m)
        h = h_inf + (self.h - h_inf)*math.exp(-dt/tau_h)
        
        self.g = self.gbar*m*m*m*h

        self.m = m
        self.h = h


class KV(Conductance):
 
    def __init__(self, gbar=18.0006, e_rev=-90):
        Conductance.__init__(self, gbar, e_rev)
        self.n = 0.0

    def integrate(self, v, dt):
        n_inf = 1/(1+math.exp((v+12.3)/-11.8))
        tau_n = 7.2 - (6.4/(1+math.exp((v+28.3)/-19.2)))
    
        n = n_inf + (self.n - n_inf)*math.exp(-dt/tau_n)
        
        self.g = self.gbar*n*n*n*n
    
        self.n = n


class LV(Conductance):

    def __init__(self, gbar=0.0187, e_rev=-50):
        Conductance.__init__(self, gbar, e_rev)
        self.g = self.gbar

    def integrate(self, v, dt):
        pass

