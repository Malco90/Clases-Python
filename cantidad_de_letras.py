##Crea una lista con el abecedario y muestra la lista.
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cadena = input("Ingrese una cadena: ")
cadena = cadena.lower()
cantidad = []
for i in abecedario:
    contador = 0
    for j in cadena:
        if i == j:
            contador += 1
    cantidad.append(contador)
for n in range(len(cantidad)):
    if cantidad[n] > 0:
        print(abecedario[n], ':', cantidad[n])

