import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.patches as mpatches

fig = plt.figure()

width = 1
height = 2
N_periods = 2

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = mpatches.FancyBboxPatch(xy=(5, 5), width=width, height=height, boxstyle=mpatches.BoxStyle("Round", pad=0.2))
ax.add_patch(patch)

def animate(i):
    x = 10/360/N_periods*i
    y = 5 + 3 * np.sin(np.radians(i)) - height/2
    patch.set_x(x)
    patch.set_y(y)
    return patch,

anim = animation.FuncAnimation(fig, animate, frames=N_periods*360, interval=5, blit=True)

ax.set_title('Анімований прямокутник із округленими краями')
plt.grid(True)
plt.show()

# writergif = animation.PillowWriter(fps = 30)
# anim.save('fancybox.gif', writer = writergif)