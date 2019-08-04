import math


class Neuron:
    
    def __init__(self, starting_voltage):
        self._voltage = starting_voltage
        self._m = 0.0
        self._n = 0.0
        self._h = 0.0
        self._sum_g = 0.0
        self._sum_ge = 0.0


    def integrate(self, dt, i_ext=0.0):

        self._sum_g = 0.0
        self._sum_ge = 0.0

        self.integrate_I_NA(dt)
        self.integrate_I_K(dt)
        self.integrate_I_L(dt)

        self._sum_ge += i_ext

        v = self._voltage
        v_inf = self._sum_ge/self._sum_g
        self._voltage = v_inf + (v - v_inf)*math.exp(-dt*self._sum_g)

        return self._voltage


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










