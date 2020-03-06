# File: animate.py
'''
This module draws in real time the voltage trace from a given neuron.
This is purely a visualization tool, and does not store any
recorded data. To save generated data for later analysis see 
datagen.py

'''

#bio libraries
import neuron, conductance
#drawing libraries
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#(voltage in mV, current in nA, time in ms)
START_VOLTAGE = -70
EXT_CURRENT = 0.5
TIME_STEP = 0.1


class PlotNeuron:
    '''
    This class is fed a matplotlib axis and a neuron to keep
    track of, applies an external current and draws the resulting
    voltage trace.
    '''

    def __init__(self, ax, neuron, maxt=200, dt=TIME_STEP):
        self.neuron = neuron

        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.vdata = [0]
        self.line = Line2D(self.tdata, self.vdata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-100, 100)
        self.ax.set_xlim(0, self.maxt)

    def getdata(self):
        '''
        This generates the next voltage point for the neuron.
        '''
        yield self.neuron.integrate(self.dt, EXT_CURRENT)

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
    nn = neuron.Neuron(START_VOLTAGE)
    nn.add_cond(conductance.NaV())
    nn.add_cond(conductance.KV())
    nn.add_cond(conductance.LV())

    fig, ax = plt.subplots()
    scope = PlotNeuron(ax,nn)

    
    ani = animation.FuncAnimation(fig, scope.update, scope.getdata, interval=10,
                                  blit=True)

    plt.show()

if __name__ == '__main__':
    main()

