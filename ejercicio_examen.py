import matplotlib.pyplot as plt
import numpy as np

l = float(input('Ingrese el valor que tomará "l": '))
ac = l**2 
at = (3**(1/2)*l**2)/4

print('El área del cuadrado es:', ac )
print('El área del triángulo es', at )
print('El área total de la figura es:', ac + at )

x = np.arange(l-10, l+9, 0.001)
y = x**2 + (3**(1/2)*x**2)/4

plt.plot(x,y, 'blue')  # función
plt.plot(x,0*x, 'red')  # eje horizontal
plt.plot(0*x, y, 'red') # eje vertical
plt.plot(l*(x/x), y, 'yellow') # eje dado por el usuario
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de f(x)')
plt.grid()
plt.show()
