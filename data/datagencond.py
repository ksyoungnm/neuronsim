# File: datagencond.py
'''
Here's just a really simple example of a script
that runs the neuron simulation for a set time
and external current, and dumps the data to a
csv. This one also dumps data from the different
ion conductances so that can be visualized as well.

'''
import model.neuron
import model.conductance

import csv

OUTFILE = 'data/condout.csv'
#(voltage in mV, current in nA, time in ms)
START_VOLTAGE = -70
EXT_CURRENT = 0.5
TIME_STEP = 0.1
MAX_TIME = 100


def main():
    fieldnames = ['Time','Voltage','gNA','gK','gL']
    with open(OUTFILE,'w',newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerow(fieldnames)

        nn = model.neuron.Neuron(START_VOLTAGE)
        nn.add_cond(model.conductance.NaV())
        nn.add_cond(model.conductance.KV())
        nn.add_cond(model.conductance.LV())

        t=0
        while t < MAX_TIME:
            v = nn.integrate(TIME_STEP,EXT_CURRENT) 
            gNA = nn._conds[0].get_g()
            gK = nn._conds[1].get_g()
            gL = nn._conds[2].get_g()           
            
            datawriter.writerow([t,v,gNA,gK,gL])
            
            t += TIME_STEP
            

if __name__ == '__main__':
    main()
