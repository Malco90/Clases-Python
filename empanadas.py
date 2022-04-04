personas = int(input('Ingrese la cantidad de personas: '))
suma = 0
n = 0
while n<personas:
    empanadas = int(input('Ingrese la cantidad de empanadas: '))
    suma = empanadas + suma
    n = n + 1
docenas = suma//12
resto = suma%12
print('Se tiene que pedir ', docenas, 'docenas, y sobran', resto, 'empanadas')