print ('Comenzar')
num = int(input('ingrese numero: '))
resto = int(num % 2)
pares = 0
impares = 0
while num != 0:
    if resto == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    num = int(input('ingrese numero: '))
    resto = int(num % 2)

print('Hay', pares, 'numeros pares y', impares, 'numeros impares')
print('Fin')