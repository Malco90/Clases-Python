x = int(input('Ingrese valor: '))
n = 0
suma = 0
while x!=0:
    suma = suma + x
    n = n + 1
    x = int(input('Ingrese valor: '))
promedio = suma/n
print('El promedio es: ', promedio)