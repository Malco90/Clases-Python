import matplotlib.pyplot as plt
import numpy as np
l = float(input('Ingrese el valor que tomará "l": '))
areacuadr = l**2
areatrian = ((3**(1/2))*(l**2))/4
areatotal = areacuadr + areatrian
print('El área total de la figura es igual a: ',areatotal)
print('Ahora graficaremos la función de ese área')
l = np.arange((l-60),(l+50),0.001)
y = (l**2)+(((3**(1/2))*(l**2))/4)
plt.plot(l,y)
plt.xlabel('l')
plt.ylabel('A(l)')
plt.title('Gráfica de A(l)')
plt.grid()
plt.show()