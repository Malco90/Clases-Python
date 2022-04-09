dinero = int(input("Cuanto dinero necesita extraer? "))
cant_mil = dinero // 1000
cant_quinientos = (dinero % 1000) // 500
cant_cien = ((dinero % 1000) % 500) // 100
cant_cincuenta = (((dinero % 1000) % 500) % 100) // 50
cant_diez = ((((dinero % 1000) % 500) % 100) % 50) // 10

if dinero % 10 == 0:
    print("Puede extraer", dinero, "pesos")
    print("Cantidad de billetes de 1000: ", cant_mil)
    print("Cantidad de billetes de 500: ", cant_quinientos)
    print("Cantidad de billetes de 100: ", cant_cien)
    print("Cantidad de billetes de 50: ", cant_cincuenta)
    print("Cantidad de billetes de 10: ", cant_diez)
else:
    print("No puede extraer", dinero, "pesos")
    
