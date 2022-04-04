import matplotlib.pyplot as plt
import numpy as np

print('COMENZAR')
print('Vamos analizar la función lineal de la forma')
print('f(x) = a·x + b')
a = int(input('Ingrese el término a: '))
b = int(input('Ingrese el término a: '))

if a>0:
    print('La función es creciente')
elif a==0:
    print('La función es una constante')
else:
    print('La función es decreciente')

print('La pendiente es: ', a)
print('y la ordenada al origen es: ', b)
print('Ahora vamos a graficar')

x = np.arange(-5,10,0.1)
yp = np.arange(-5,10,0.1)
y = a*x+b
plt.plot(x,y)
plt.plot(x, np.full(x.shape, 0))
plt.plot(yp, np.full(yp.shape, 0))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica')
plt.grid(True, which = 'both')
plt.show()
