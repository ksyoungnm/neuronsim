import csv
import neuron
import time
import conductance
import HHconductance
import config

# set integration timestep (ms)
TIME_STEP = config.neuronConfig['time_step']
# set starting voltage (mV)
START_VOLTAGE = config.neuronConfig['starting_v']

fieldnames = ["time","voltage"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

n = neuron.Neuron(START_VOLTAGE)
n.add_cond(conductance.NaV())
n.add_cond(conductance.KV())
n.add_cond(conductance.LV())

t = 0.0
v = START_VOLTAGE

if config.generalconfig['mode'] == 'animate':
    import tkinter as tk
    root = tk.Tk()
    scale = tk.Scale(root, from_=1.0, to_=-1.0, resolution=0.1)
    scale.pack()

    def write_val():
        global t,v,n
        with open('data.csv','a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
            info = {
                "time": t,
                "voltage": v
            }
            csv_writer.writerow(info)
            print(t, v)
            t += TIME_STEP
            v = n.integrate(TIME_STEP, i_ext=scale.get())
    
        root.after(15, write_val)
    
    root.after(0,write_val)
    root.mainloop()
    
else:
    while t < 1000:
    
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
            info = {
                "time": t,
                "voltage": v
            }
            csv_writer.writerow(info)
            print(t, v)
            t += TIME_STEP
            v = n.integrate(TIME_STEP, config.neuronConfig['i_ext'])
    

