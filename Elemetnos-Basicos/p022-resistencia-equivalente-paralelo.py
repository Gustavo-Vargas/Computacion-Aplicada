# p022-resistencia-equivalente-paralelo.py
# Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.
# El programa debe solicitar al usuario que ingrese el valor de cada una de las cuatro resistencias (R1, R2, R3 y R4).
# Luego, debe calcular la resistencia total usando la siguiente fórmula:
# rt = 1 / ( (1/r1) + (1/r2) + (1/r3) )

print("-" * 40)
print('Calcular resistencia equivalente en paralelo')   
print("-" * 40)

# Entrada
r1 = float(input('Ingrese el valor de la resistencia R1: '))
r2 = float(input('Ingrese el valor de la resistencia R2: '))
r3 = float(input('Ingrese el valor de la resistencia R3: '))

# Proceso
rt = 1 / ( (1/r1) + (1/r2) + (1/r3) )

# Salida
print("-" * 40)
print(f'La resistencia total es: {rt:.2f}')
print("-" * 40)


