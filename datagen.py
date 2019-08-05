import csv
import neuron
import time
import conductance

# set integration timestep (ms)
TIME_STEP = 0.1
# set starting voltage (mV)
START_VOLTAGE = -50

fieldnames = ["time","voltage"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

n = neuron.Neuron(START_VOLTAGE)
n.add_cond(conductance.NaConductance())
n.add_cond(conductance.KConductance())
n.add_cond(conductance.LConductance())

t = 0.0
v = START_VOLTAGE

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "time": t,
            "voltage": v
        }
        csv_writer.writerow(info)
        print(t, v)
        t += TIME_STEP
        v = n.integrate(TIME_STEP, i_ext=0.2)

        time.sleep(0.005)

