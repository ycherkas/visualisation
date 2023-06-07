# Побудуйте тривимірну візуалізацію векторного поля
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

x, y, z = np.meshgrid(np.arange(-10, 10, 2.5),
                      np.arange(-10, 10, 2.5),
                      np.arange(-10, 10, 2.5))

u = (x + z)/x**2
v = 1/y
w = 1/z

ax = plt.figure().add_subplot(projection='3d')
ax.quiver(x, y, z, u, v, w, length=2, color = 'black')
plt.title(r'$F=(\frac{x+z}{x^2}; \frac{1}{y}; \frac{1}{z})$')
plt.show()