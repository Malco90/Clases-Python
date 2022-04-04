x = int(input('Ingrese valor: '))
n = 1
numeros = []
lista_de_divisores = []
while n <= x:
    numeros.append(n)
    contador = 0
    for i in range(1, n+1):
        if (n % i) == 0:
            contador += 1
    lista_de_divisores.append(contador)
    n += 1
cant = max(lista_de_divisores)
num = lista_de_divisores.index(cant)+1
print('El número con más divisores es:', num,'con', cant, 'divisores.')

lista_de_divisores = []
for j in range(1, num):
        if (num % j) == 0:
            lista_de_divisores.append(j)
print(lista_de_divisores)