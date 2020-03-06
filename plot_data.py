import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
t = data['time']
v = data['voltage']
plt.figure(figsize=(5,2.5))
plt.plot(t,v)
plt.xlim(0,800)
plt.grid()
plt.show()
