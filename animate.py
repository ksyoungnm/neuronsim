# File: animate.py
'''
This module draws in real time the voltage trace from a simulated neuron.
Current can be applied using the slider at the bottom. This module doesn't
save any data, just meant to be a visualization tool.
'''

#bio libraries
import model.neuron
import model.conductance
# import model.HHconductance

#config stuff
import json
CONFIGFILE = 'model/config.json'
with open(CONFIGFILE) as configfile:
        CONFIG = json.load(configfile)
#drawing libraries
from matplotlib.lines import Line2D
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class PlotNeuron:
    '''
    This class is fed a matplotlib axis and a neuron to keep
    track of, applies an external current and draws the resulting
    voltage trace.
    '''

    def __init__(self, ax, neuron, ext_current=0, maxt=200, dt=0.1):
        self.neuron = neuron
        self.ext_current = ext_current

        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.vdata = [0]
        self.line = Line2D(self.tdata, self.vdata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-100, 100)
        self.ax.set_xlim(0, self.maxt)

    def setcurrent(self, current):
        self.ext_current = current

    def getdata(self):
        '''
        This generates the next voltage point for the neuron.
        '''
        yield self.neuron.integrate(self.dt, self.ext_current)

    def update(self, v):
        '''
        This just draws the result of the above method, also
        changing the axes if we go over.
        '''
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:
            self.tdata = [self.tdata[-1]]
            self.vdata = [self.vdata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.vdata.append(v)
        self.line.set_data(self.tdata, self.vdata)
        return self.line,

def main():
    start_v     = CONFIG['neuronConfig']['start_v']
    ext_current = CONFIG['neuronConfig']['ext_current']
    time_step   = CONFIG['neuronConfig']['time_step']

    nn = model.neuron.Neuron(start_v)
    nn.add_cond(model.conductance.NaV())
    nn.add_cond(model.conductance.KV())
    nn.add_cond(model.conductance.LV())

    fig, (ax, curr) = plt.subplots(2,1, gridspec_kw={'height_ratios':[11,1]})
    scope = PlotNeuron(ax,nn,
                       ext_current=ext_current,
                       dt=time_step)

    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Voltage (mV)')

    scurr = Slider(curr, 'Applied Current (nA)', -1, 5, valinit=1, valstep=0.1)
    scurr.on_changed(scope.setcurrent)

    ani = animation.FuncAnimation(fig, scope.update, scope.getdata, interval=5, blit=True)
    fig.tight_layout()

    plt.show()

if __name__ == '__main__':
    main()
