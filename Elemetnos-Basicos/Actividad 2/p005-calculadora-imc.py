# - p005-calculadora-imc.py
# Calcula el indice de masa corporal

print('Calculadno el indice de masa corporal (IMC) \n')

# Entrada 
peso_kg = float( input('Ingresa tu peso en kilogrammos: '))
altura_m = float( input('Ingresa tu altura en metros: '))

# Proceso
imc = peso_kg / (altura_m ** 2) # divide el peso entre la latura al cuadradop (** eleva a la potencia)

# Salida
print("\nEl peso es {0:.2f}Kg, la altura es {1:.2f}m y resulta en un IMC de {2:.2f}".format(peso_kg, altura_m, imc) )

print(f"\nEl peso es {peso_kg:.2f}Kg, la altura es {altura_m:.2f}m y resulta en un IMC de {imc:.2f}" )

