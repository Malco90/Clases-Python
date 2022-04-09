## Convertir un número decimal a binario
numero = int(input("Introduce un número decimal: "))
binario = ""
while numero > 0:
    binario = str(numero % 2) + binario
    numero = numero // 2
print("El número binario es:", binario)
longitud_binario = len(binario)
print("La longitud del número binario es:", longitud_binario)
