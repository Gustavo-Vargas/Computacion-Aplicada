# p043-adivina-numero.py
# Simula un juego de azar donde le usauroi adivina un numero entre 1 y 50

import random

print('\033[2J\033[H')
print('Bienvenido al juego de Adivina número ...')
print('YO te doy un número entre 1 y 50 y tu tratas de adivinarlo')

numero_secreto = random.randint(1,50)
intento_usuario = 0
contador_intentos = 0

while True:
    intento_usuario = int(input('Tu numero: '))
    contador_intentos += 1
    
    if intento_usuario < numero_secreto:
        print('Demasiado BAJO, Intenta con un número más alto')
    elif intento_usuario > numero_secreto:
        print('Demasiado ALTO, Intenta con un número más bajo')
    else: 
        print(f'\nFelicidades, Adivinaste el numero secreto : {numero_secreto}')
        print(f'Lo lograste en {contador_intentos} intentos !')
        break
    
    
