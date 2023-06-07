#Побудувати графік у полярних координатах
import numpy as np
import matplotlib.pyplot as plt

alfa = 1
fi = np.arange(-np.pi/2, np.pi/2, 0.001)
r1 = alfa * (1 + np.sin(fi)) / np.cos(fi)
r2 = alfa * (1 - np.sin(fi)) / np.cos(fi)

ax = plt.subplot(111, projection='polar')
ax.plot(fi, r1, label=r'$\rho=\alpha\frac{1 + \sin(\phi)}{\cos(\phi)}$')
ax.plot(fi, r2, label=r'$\rho=\alpha\frac{1 - \sin(\phi)}{\cos(\phi)}$')
ax.legend()
ax.set_rmax(5)
plt.show()