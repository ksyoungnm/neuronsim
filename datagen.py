# File: datagen.py
'''
This module generates and stores data from the neuron model
for later analysis. For real-time visualization see animate.py

'''

import neuron, conductance
import numpy,csv

OUTFILE = 'data/out.csv'
#(voltage in mV, current in nA, time in ms)
START_VOLTAGE = -70
EXT_CURRENT = 0.5
TIME_STEP = 0.1
MAX_TIME = 10


def main():
    with open(OUTFILE,'w',newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerow(['Time','Voltage'])

        nn = neuron.Neuron(START_VOLTAGE)
        nn.add_cond(conductance.NaV())
        nn.add_cond(conductance.KV())
        nn.add_cond(conductance.LV())

        t = 0
        while t < MAX_TIME:
            v = nn.integrate(TIME_STEP,EXT_CURRENT)
            datawriter.writerow([t,v])
            t += TIME_STEP

if __name__ == '__main__':
    main()

