#p002-area-circulo.py
# Calcula el area de un circulo
import math # im-ortamos el modulo math para constantes y funciones matematicas

print( 'Calculando el area de un circulo : \n')

# Entrada
print('Dame el radio : ')
radio = float( input() )

# Proceso
area = math.pi * math.pow(radio, 2) 

# Salida
print(f'EL circulo de radio {radio:.2} tiene un area de {area:,.2f}')

