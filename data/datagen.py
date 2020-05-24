# File: datagen.py
'''
Here's just a really simple example of a script
that runs the neuron simulation for a set time
and external current, and dumps the data to a
csv.

'''

import model.neuron
import model.conductance

import numpy,csv

OUTFILE = 'data/out.csv'
#(voltage in mV, current in nA, time in ms)
START_VOLTAGE = -70
EXT_CURRENT = 0.5
TIME_STEP = 0.1
MAX_TIME = 100

def main():
    with open(OUTFILE,'w',newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerow(['Time','Voltage'])

        nn = model.neuron.Neuron(START_VOLTAGE)
        nn.add_cond(model.conductance.NaV())
        nn.add_cond(model.conductance.KV())
        nn.add_cond(model.conductance.LV())

        t = 0
        while t < MAX_TIME:
            v = nn.integrate(TIME_STEP,EXT_CURRENT)
            datawriter.writerow([t,v])
            t += TIME_STEP

if __name__ == '__main__':
    main()

