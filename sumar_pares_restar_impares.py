x = int(input('Ingrese valor: '))
suma = 0
while x!=0:
    resto = x%2
    if resto==0:
        suma = suma + x
    else:
        suma = suma - x
    x = int(input('Ingrese valor: '))
print('La suma es:', suma)