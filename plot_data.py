import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
t = data['time']
v = data['voltage']
plt.plot(t,v)
plt.show()
