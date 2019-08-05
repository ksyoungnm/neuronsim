import math


class Neuron:
    
    def __init__(self, starting_voltage):
        self._voltage = starting_voltage
        self._conds = []

        self._sum_g = 0.0
        self._sum_ge = 0.0

    def add_cond(self, cond):
        self._conds.append(cond)

    def integrate(self, dt, i_ext=0.0):
        self._sum_g  = 0.0
        self._sum_ge = 0.0

        for cond in self._conds:
            cond.integrate(self._voltage, dt)
            self._sum_g  += cond.get_g()
            self._sum_ge += cond.get_ge()

        self._sum_ge += i_ext

        v = self._voltage
        v_inf = self._sum_ge/self._sum_g
        self._voltage = v_inf + (v - v_inf)*math.exp(-dt*self._sum_g)

        return self._voltage









