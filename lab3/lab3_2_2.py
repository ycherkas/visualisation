# Побудуйте візуалізацію плоского векторного поля як за допомогою 
# векторів та ліній току з бібліотеки matplotlib та за допомогою коду з лістингу;
import numpy as np
import matplotlib.pyplot as plt

def u(x, y):
    return y*x**2
def v(x, y):
    return -y

def create_stream_line(x0, y0, u, v, t0=0, t1=0.001, dt=0.0001):
    t = np.arange(t0, t1, dt)
    xx_new = np.zeros_like(t)
    yy_new = np.zeros_like(t)
    xx_new[0] = x0
    yy_new[0] = y0

    for i in range(1, t.size):
        xx_new[i] = x0 + u(x0, y0) * dt
        yy_new[i] = y0 + v(x0, y0) * dt
        x0, y0 = xx_new[i], yy_new[i]

    return xx_new, yy_new


for i in range(-10, 10):
    for j in range(-10, 10):
        x1, y1 = create_stream_line(i, j, u, v)
        plt.plot(x1, y1)

plt.title('Лінії току ' + r'$F = (x^2y; -y)$')
plt.show()
