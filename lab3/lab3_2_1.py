# Побудуйте візуалізацію плоского векторного поля як за допомогою 
# векторів та ліній току з бібліотеки matplotlib та за допомогою коду з лістингу;
import numpy as np
import matplotlib.pyplot as plt

def u(x, y):
    return y*x**2
def v(x, y):
    return -y

xx, yy = np.meshgrid(np.linspace(-10, 10, 10), np.linspace(-10, 10, 10))
u_val = u(xx, yy)
v_val = v(xx, yy)

plt.quiver(xx, yy, u_val, v_val)
plt.title('Векторне поле ' + r'$F = (x^2y; -y)$')

fig, ax = plt.subplots()
plt.streamplot(xx, yy, u_val, v_val)
plt.title('Лінії потоку ' + r'$F = (x^2y; -y)$')
plt.show()