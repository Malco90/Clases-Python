x = int(input('Ingrese la cantidad de terminos a sumar: '))
n = 0
suma = 0
while n <= x:
    ter = ((-1)**n)/(2*n+1)
    suma = ter + suma
    n = n + 1
print('La suma total es de , ', suma*4)