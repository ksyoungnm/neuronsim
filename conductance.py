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


class HHNa(Conductance):

    def __init__(self, gbar=95.0174, e_rev=60):
        Conductance.__init__(self, gbar, e_rev)
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
        Conductance.__init__(self, gbar, e_rev)
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



class HHL(Conductance):
    
    def __init__():
        pass

    def integrate():
        pass


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
        
        

