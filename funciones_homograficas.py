import matplotlib.pyplot as plt
import numpy as np
print('Vamos a analizar la función homográfica de la forma f(x)=(ax+b)/(cx+d)')
a = float(input('Ingrese el valor que tomará "a": '))
b = float(input('Ingrese el valor que tomará "b": '))
c = float(input('Ingrese el valor que tomará "c": '))
d = float(input('Ingrese el valor que tomará "d": '))
print('Analicemos los datos necesarios para graficar a f(x)')
ord = b/d
raiz = -b/a
ah = a/c
av = -d/c
print("La Asíntota Horizontal es igual a: ",ah)
print("La Asíntota Vertical es igual a: ",av)
print("La Raíz es igual a: ", raiz)
print("La Ordenada al Origen es: ", ord)
print('Ahora a graficar')
i = int(input('¿Desde dónde quiere comenzar la gráfica?: '))
f = int(input('¿Hasta dónde quiere graficar?: '))
x = np.arange(i, f+1, 0.001)
y = ((a*x) + b) / ((c*x) + d)
plt.plot(x,y, 'blue')  # función
plt.plot(x,0*x, 'red')  # eje horizontal
plt.plot(0*x, y, 'red') # eje vertical
plt.plot(x, ah*(x/x), 'orange')  # asintota horizontal
plt.plot(av*(x/x), y, 'orange') # asintota vertical 
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de f(x)')
plt.grid()
plt.show()
