import matplotlib.pyplot as plt
import pandas as pd

filename = 'condout.csv'

data = pd.read_csv(filename)
t = data['Time']
v = data['Voltage']
gNA = data['gNA']
gK = data['gK']
gL = data['gL']

fig, axs = plt.subplots(3, sharex=True)
axs[0].plot(t,v)
axs[0].set(ylabel="Voltage (mV)")
axs[1].plot(t,gNA)
axs[1].set(ylabel="gNA (uS)")
axs[2].plot(t,gK)
axs[2].set(ylabel="gK (uS)")


for ax in axs:
    ax.grid(True)
    ax.set_xlim(0,110)

# plt.show()
plt.savefig('spikeconds')
