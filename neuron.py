import math

class Neuron:
    
    def __init__(self, starting_voltage):
        self._voltage = starting_voltage
        self._conds = []

    def add_cond(self, cond):
        self._conds.append(cond)

    def integrate(self, dt, i_ext):
        sum_g  = 0.0
        sum_ge = 0.0

        for cond in self._conds:
            cond.integrate(self._voltage, dt)
            sum_g  += cond.get_g()
            sum_ge += cond.get_ge()

        sum_ge += i_ext

        v = self._voltage
        v_inf = sum_ge/sum_g
        self._voltage = v_inf + (v - v_inf)*math.exp(-dt*sum_g)

        return self._voltage









