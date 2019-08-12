import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    ax.set_ylim(-100, 60)
    ax.set_xlim(0, 500)
    del t[:]
    del v[:]
    line.set_data(t, v)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
t, v = [], []


def animate(i):
    # update the data
    data = pd.read_csv('data.csv')
    t = data['time']
    v = data['voltage']


    xmin, xmax = ax.get_xlim()
    l_edge = xmax-50
    recent_t = t[len(t)-1] 

    if recent_t >= l_edge:
        ax.set_xlim(xmin+0.5, xmax+0.5)
        ax.figure.canvas.draw()
    line.set_data(t, v)

    return line,

ani = animation.FuncAnimation(fig, animate,
                                interval=1,
                                init_func=init,
                                blit=True)
plt.show()

