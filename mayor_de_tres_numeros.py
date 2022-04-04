print('INICIO')
a = int(input('Ingrese primer número: '))
b = int(input('Ingrese segundo número: '))
c = int(input('Ingrese tercer número: '))

if a>b:
    if b>c:
        print('El numero mayor es: ', a)
    else:
        print('El numero mayor es: ', c)
else:
    if b>c:
        print('El numero mayor es: ', b)
    else:
        print('El numero mayor es: ', c)
print('FIN')