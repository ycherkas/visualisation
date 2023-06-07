#Візуалізація скалярного поля. Знайдіть його градієнт та візуалізуйте його як плоске векторне поле;
import numpy as np
from matplotlib import pyplot as plt

n = 20
x = np.linspace(-10., 10., n) # діапазон по X
y = np.linspace(-10., 10., n) # діапазон по Y
X, Y = np.meshgrid(x, y)
Z = 7 * np.log(X ** 2 + 1/13) + 4 * np.sin(X * Y) # Формула скалярного поля
Z_dx, Z_dy = np.gradient(Z)

# Векторне поле
plt.quiver(X, Y, Z_dx, Z_dy)
plt.title('Векторне поле ' + r'$u(x,y)=-7\ln(x^2+1/13) + 4\sin(xy)$')

# Лінії потоку поля
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.streamplot(X, Y, Z_dx, Z_dy, color=Z, cmap='viridis')
plt.title('Лінії потоку поля ' + r'$u(x,y)=-7\ln(x^2+1/13) + 4\sin(xy)$')
plt.show()