# p015-hipotenusa-triangulo.py
# Calcular la hipotenusa de un triangulor ectangulo
# Se desea calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados, usando la siguiente formula:
#  • hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )

import math as mt

print("-" * 40)
print('Hipotenusa de triangulo')
print("-" * 40)

# Entrada 
lado1 = float(input('Ingrese el valor del lado 1: '))
lado2 = float(input('Ingrese el valor del lado 2: '))
lado3 = float(input('Ingrese el valor del lado 3: '))

# Proceso
hipotenusa = mt.sqrt(lado1 * lado1 + lado2 * lado2)

# Salida
print("Valores ingresados:")
print(f'Lado 1: {lado1},  Lado 2: {lado2},  Lado 3: {lado3}')
print(f'La hipotenusa del triangulo es: {hipotenusa:.2f}')
