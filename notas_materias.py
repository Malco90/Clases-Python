materias=int(input("inserte cantidad de materias: "))
n = 0
suma = 0
while n < materias:
    nombre=(input("inserte nombre de la materia: "))
    nota=int(input("ingrese nota de la materia: "))
    
    if nota >= 6:
        print("materia aprobada")
    else:
        print("materia reprobada")
    n=n+1
    suma = suma + nota

promedio = suma / materias
print("el promedio es: ", promedio)
print("fin del programa")