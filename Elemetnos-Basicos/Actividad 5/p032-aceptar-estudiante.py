# p032-aceptar-estudiante.py
# Aceptar a un estudiante en base a la edad y 2 calificaciones
# usaremos or

print('\033[2J\033[H')
print(' --- Admision de estudiatnes a la UNiversidad Sierra Madres ---')

nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

if edad < 18:
    print(f'Lo sentimos, {nombre}. Solo aceptamos mayores de edad, y tu tienes tan solo {edad}')
else:
    print('Ingresa 2 calificaciones separadas por Enter')
    calificacion1 = float(input())
    calificacion2 = float(input())
    if calificacion1 < 8 or calificacion2 < 9:
        print(f'Lo sentimos, se require 2 calificaciones de 8 minimo, y tu tiens {calificacion1}, {calificacion2}')
    else:
        print(f'!Bienvenido {nombre}, tu edad {edad} y tus calificaciones: {calificacion1}, {calificacion2} te permiten ingresar')
        
    
    
    

print('\nProceso Terminado ')
