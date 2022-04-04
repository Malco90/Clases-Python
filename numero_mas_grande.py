valor1 = int(input('Ingrese primer valor: '))
valor2 = int(input('Ingrese segundo valor: '))

if valor1 < valor2:
    print(valor2, 'Es mayor')
elif valor1 == valor2:
    print('Los valores son iguales')
else:
    print(valor1, 'Es mayor')

print('FIN')