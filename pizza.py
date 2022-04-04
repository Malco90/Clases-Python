pizzas = int(input('Ingrese la cantidad de pizzas: '))
personas = int(input('Ingrese la cantidad de personas: '))

porciones = pizzas*8
ppp = porciones//personas
resto = porciones%personas

print('Le corresponde ', ppp, 'porciones por personas, y sobran', resto, 'porciones.')