# File: conductance.py
'''
This module contains implementations of the different kinds of
conductance models. Parameters were found from:

O’Leary, T., & Marder, E. (2016). Temperature-Robust Neural 
Function from Activity-Dependent Ion Channel Regulation. 
Current Biology, 26(21), 2935–2941. 
https://doi.org/10.1016/j.cub.2016.08.061.

To define a conductance, we have to provide a few things: 
a gbar parameter (think how many ion channels per unit membrane),
and a reversal potential e_rev (voltage at which there is no
net flow of a certain ion species across a membrane). Additionally,
the different ion channels react with different current and time
dynamics, so we need to provide the equations by which these
things happen. Therefore ovexrwriting the integrate method is also
required.
'''
import math

# config stuff
import json
from os import path
CONFIGFILE = path.join(path.dirname(__file__),'config.json')
with open(CONFIGFILE) as configfile:
    config = json.load(configfile)

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


class NaV(Conductance):

    def __init__(self, gbar  = config['condConfig']['NaV']['gbar'],
                       e_rev = config['condConfig']['NaV']['e_rev']):

        super().__init__(gbar, e_rev)
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

    def __init__(self, gbar  = config['condConfig']['KV']['gbar'],
                       e_rev = config['condConfig']['KV']['e_rev']):

        super().__init__(gbar, e_rev)
        self.n = 0.0

    def integrate(self, v, dt):
        n_inf = 1/(1+math.exp((v+12.3)/-11.8))
        tau_n = 7.2 - (6.4/(1+math.exp((v+28.3)/-19.2)))
    
        n = n_inf + (self.n - n_inf)*math.exp(-dt/tau_n)
        
        self.g = self.gbar*n*n*n*n
    
        self.n = n


class LV(Conductance):

    def __init__(self, gbar  = config['condConfig']['LV']['gbar'],
                       e_rev = config['condConfig']['LV']['e_rev']):

        super().__init__(gbar, e_rev)
        self.g = self.gbar

    def integrate(self, v, dt):
        pass

