materias = ['Matematica', 'Física', 'Educación fisica', 'Arte', 'Historia']
n = 0

while n<5:
    print( materias[n])
    nota = int(input('Ingrese la nota: '))
    if nota < 6:
        print('Desaprobado')
    else:
        print('Aprobado')
    n = n + 1
    print('')