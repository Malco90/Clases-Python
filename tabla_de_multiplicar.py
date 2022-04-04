print('INICIO')
x = int(input('Mostrar la tabla del: '))
n = 0

while n<11:
    tabla = n * x
    print(x, '*', n, '=', tabla)
    n = n + 1
print('FIN')