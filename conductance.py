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


class NaConductance(Conductance):

    def __init__(self, gbar=95.0174, e_rev=60):
        Conductance.__init__(self, gbar, e_rev)
        self.n = 0.0
        self.h = 0.0

    def integrate(self, v, dt):
        n_inf = 1/(1+math.exp((v+25.5)/-5.29))
        tau_n = 1.32 - (1.26/(1+math.exp((v+120)/-25)))
    
        h_inf = 1/(1+math.exp((v+48.9)/5.18))
        tau_h = (0.67/(1+math.exp((v+62.9)/-10)))*(1.5 + (1/(1+math.exp((v+34.9)/3.6))))
    
        n = n_inf + (self.n - n_inf)*math.exp(-dt/tau_n)
        h = h_inf + (self.h - h_inf)*math.exp(-dt/tau_h)
        
        self.g = self.gbar*n*n*n*h

        self.n = n
        self.h = h


class KConductance(Conductance):
    
    def __init__(self, gbar=18.0006, e_rev=-90):
        Conductance.__init__(self, gbar, e_rev)
        self.m = 0.0

    def integrate(self, v, dt):
        m_inf = 1/(1+math.exp((v+12.3)/-11.8))
        tau_m = 7.2 - (6.4/(1+math.exp((v+28.3)/-19.2)))
    
        m = m_inf + (self.m - m_inf)*math.exp(-dt/tau_m)
        
        self.g = self.gbar*m*m*m*m
    
        self.m = m


class LConductance(Conductance):

    def __init__(self, gbar=0.0187, e_rev=-50):
        Conductance.__init__(self, gbar, e_rev)
        self.g = self.gbar

    def integrate(self, v, dt):
        pass
        
        




    


























    def integrate_I_K(self, dt):
        v = self._voltage

        m_0 = self._m
        m_inf = 1/(1+math.exp((v+12.3)/-11.8))
        tau_m = 7.2 - (6.4/(1+math.exp((v+28.3)/-19.2)))
    
        m = m_inf + (m_0 - m_inf)*math.exp(-0.1/tau_m)
        g = 18.0006*m*m*m*m
    
        self._m = m

        self._sum_g += g
        self._sum_ge += (-g*90)


    def integrate_I_L(self, dt):
        g = 0.0187

        self._sum_g += g
        self._sum_ge += (-g*50)

    def integrate_I_NA(self, dt):
        v = self._voltage

        n_0 = self._n
        n_inf = 1/(1+math.exp((v+25.5)/-5.29))
        tau_n = 1.32 - (1.26/(1+math.exp((v+120)/-25)))
    
        h_0 = self._h
        h_inf = 1/(1+math.exp((v+48.9)/5.18))
        tau_h = (0.67/(1+math.exp((v+62.9)/-10)))*(1.5 + (1/(1+math.exp((v+34.9)/3.6))))
    
        n = n_inf + (n_0 - n_inf)*math.exp(-0.1/tau_n)
        h = h_inf + (h_0 - h_inf)*math.exp(-0.1/tau_h)
        
        g = 95.0174*n*n*n*h

        self._n = n
        self._h = h

        self._sum_g += g
        self._sum_ge += (g*60)



