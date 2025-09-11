# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones de redondeo

import math as mt

precio = 15.65
arriba = mt.ceil(precio)  # Redondea hacia arriba
abajo = mt.floor(precio) # Redondea hacia abajo
truncar = mt.trunc(precio) # Elimina los decimales
redondeo = round(precio) # Redondea al entero más cercano
undecimal = round(precio, 1) # Redondea a un decimal

print(f'El precio original es: {precio}')
print(f'El precio redondeado hacia arriba es: {arriba}')
print(f'El precio redondeado hacia abajo es: {abajo}')
print(f'El precio truncado es: {truncar}')
print(f'El precio redondeado al entero más cercano es: {redondeo}')
print(f'El precio redondeado a un decimal es: {undecimal}')