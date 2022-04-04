print('COMENZAR')
cant = int(input('Ingrese la cantidad de términos a sumar: '))
n = 1
suma = 0

while n <= cant:
    termino = 1/(2**n)
    n = n + 1
    suma = suma + termino
print(suma)