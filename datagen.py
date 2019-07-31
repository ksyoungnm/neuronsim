import numpy as np
import csv
import time
import math


t = 0.0
v = -70.0
i = 0.0

m = 0.0
n = 0.0
h = 0.0





def I_K(v):
    global m
    m_0 = m
    m_inf = 1/(1+math.exp((v+12.3)/-11.8))
    tau_m = 7.2 - (6.4/(1+math.exp((v+28.3)/-19.2)))

    m = m_inf + (m_0 - m_inf)*math.exp(-0.1/tau_m)
    g = 18.0006*m*m*m*m

    return g*(v+90)


def I_NA(v):
    global n
    global h
    
    n_0 = n
    n_inf = 1/(1+math.exp((v+25.5)/-5.29))
    tau_n = 1.32 - (1.26/(1+math.exp((v+120)/-25)))

    h_0 = h
    h_inf = 1/(1+math.exp((v+48.9)/5.18))
    tau_h = (0.67/(1+math.exp((v+62.9)/-10)))*(1.5 + (1/(1+math.exp((v+34.9)/3.6))))

    n = n_inf + (n_0 - n_inf)*math.exp(-0.1/tau_n)
    h = h_inf + (h_0 - h_inf)*math.exp(-0.1/tau_h)

    g = 95.0174*m*m*m*h


    return g*(v-60)

def I_L(v):

    return 0.0187


fieldnames = ["time","voltage"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while t<400:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "time": t,
            "voltage": v
        }
        csv_writer.writerow(info)
        print(t, v)
        t += 0.1
        v += i

        i = I_NA(v) + I_K(v) + I_L(v)

        if t > 200 and t < 200.2:
            i += 10.0


