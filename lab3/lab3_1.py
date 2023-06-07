#Візуалізація скалярного поля.
import numpy as np
from matplotlib import pyplot as plt

n = 256
x = np.linspace(-10., 10., n) # діапазон по X
y = np.linspace(-10., 10., n) # діапазон по Y
X, Y = np.meshgrid(x, y)
Z = 7 * np.log(X ** 2 + 1/13) + 4 * np.sin(X * Y) # Формула скалярного поля

plt.xlabel('x')
plt.ylabel('y')
plt.title('Скалярне поле ' + r'$u(x,y)=-7\ln(x^2+1/13) + 4\sin(xy)$')
plt.pcolormesh(X, Y, Z)
plt.show()