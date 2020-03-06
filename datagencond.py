import csv
import neuron
import conductance
import config



TIME_STEP = config.neuronConfig['time_step']
# set starting voltage (mV)
START_VOLTAGE = config.neuronConfig['starting_v']

fieldnames = ['time','voltage','gNA','gK','gL']

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

n = neuron.Neuron(START_VOLTAGE)
n.add_cond(conductance.NaV())
n.add_cond(conductance.KV())
n.add_cond(conductance.LV())

t=0.0
v=START_VOLTAGE
gNA = n._conds[0].get_g()
gK = n._conds[1].get_g()
gL = n._conds[2].get_g()

while t < 500:
    
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        info = {
            "time": t,
            "voltage": v,
            "gNA": gNA,
            "gK": gK,
            "gL": gL
        }
        csv_writer.writerow(info)
        print(t, v)
        t += TIME_STEP
        v = n.integrate(TIME_STEP, config.neuronConfig['i_ext'])
        gNA = n._conds[0].get_g()
        gK = n._conds[1].get_g()
        gL = n._conds[2].get_g()

