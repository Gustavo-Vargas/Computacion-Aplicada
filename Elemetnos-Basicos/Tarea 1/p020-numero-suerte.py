# p020-numero-suerte.py
# Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos. A partir
# de este dato, el programa debe:
# • Mostrar cada uno de los dígitos individuales del año. Por ejemplo, si el año es 1995, debe mostrar "1", "9","9", "5".
# • Calcular y mostrar la suma de los dígitos individuales del año. Siguiendo el ejemplo anterior, la suma sería:  1 + 9 + 9 + 5 = 24.

print("-" * 40)
print('Calcular número de la suerte')
print("-" * 40)

# Entrada
anio = int(input('Ingrese su año de nacimiento (formato: AAAA): '))

# Proceso
d1 = anio // 1000        # Extrae el primer dígito
d2 = (anio // 100) % 10  # Extrae el segundo dígito
d3 = (anio // 10) % 10   # Extrae el tercer dígito
d4 = anio % 10           # Extrae el cuarto dígito
suma = d1 + d2 + d3 + d4  # Suma de los dígitos

print("-" * 40)
print(f'Los dígitos individuales de su año de nacimiento son: {d1}, {d2}, {d3}, {d4}')
print(f'La suma de los dígitos es: {suma}')

