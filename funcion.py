import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10,10,1)
f = 2*x

plt.plot(x,f)
plt.xlabel('X')
plt.ylabel('f(x)')
plt.title('Gráfica fe f(x)')
plt.grid()
plt.show()