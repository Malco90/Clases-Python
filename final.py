x = int(input('Ingrese valor'))
suma = 0
resta = 0

while x != 0:
    
    if x%2 == 0:
        print('El valor es par')
        suma = suma + x
    elif x%2 == 1:
        print("el valor es impar")
        suma = suma - x
    x = int(input("ingrese valor"))
    
print('fin del prgrama', "el resultado es", suma)