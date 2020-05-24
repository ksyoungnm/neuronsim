import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('out.csv')
t = data['Time']
v = data['Voltage']
plt.figure(figsize=(5,2.5))
plt.plot(t,v)
plt.xlim(0,110)
plt.grid()

# plt.show()
plt.savefig('spike')
