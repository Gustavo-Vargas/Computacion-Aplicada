# p017-convertir-temperatura.py
# Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit, usando la siguiente formula:
# • farenheit = (celcius × 9/5) + 32

print("-" * 40)
print('Convertir temperatura de Celcius a Farenheit')
print("-" * 40)

# Entrada
celcius = float(input('Ingrese la temperatura en grados Celcius: '))

# Proceso
farenheit = (celcius * 9/5) + 32

# Salida
print("-" * 40)
print(f'La temperatura en grados Farenheit es: {farenheit:.2f}')
print("-" * 40)
