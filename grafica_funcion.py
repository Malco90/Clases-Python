import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)
y = x**2+3*x+8
plt.plot(x,y, color = 'green')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de f(x)')
plt.grid()
plt.show()