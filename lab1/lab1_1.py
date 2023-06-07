#Побудувати графіки функцій
import numpy as np 
import matplotlib.pyplot as plt 

def f1(x): 
   return (2+(np.sin(x))**3)/(1 + x**2)

def f2(x):
    if x <= 0:
        return (5*(x**2))/(1 + x**2)
    else:
        return np.sqrt(1+2*x/(1+x**2))

x = np.arange(-5, 5, 0.02)
x1 = x[x <= 0]
x2 = x[x > 0]

plt.figure(1) 
plt.subplot(211) 
plt.plot(x, f1(x), 'k')
plt.legend([r'y=$\frac{2+sin(x)^3}{1+x^2}$'])
plt.grid(True)
plt.ylabel(r'y') 

f21_vals = list(map(f2, x1))
f22_vals = list(map(f2, x2))
plt.subplot(212) 
plt.plot(x1, f21_vals, 'r')
plt.plot(x2, f22_vals, 'y')
plt.legend([r'z=$\frac{5x^2}{1+x^2}$', r'z=$\sqrt{1+\frac{2x}{1+x^2}}$'])
plt.grid(True)
plt.xlabel('x')
plt.ylabel('z')
plt.show()