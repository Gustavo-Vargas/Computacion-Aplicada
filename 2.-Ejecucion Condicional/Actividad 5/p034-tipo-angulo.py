# p034-tipo-angulo.py
# Mostrar el tipo de angulo
# <90 Agudo, =90 Recto, <100 Obtuso, =180 llano, <360Concavo, = 
print('\033[2J\033[H')
print('--- Clasificacion de Angulos de acuerdo a su magnitud ---')

angulo = int(input('Dame un agnulo en grados ? '))

if angulo < 0 or angulo > 360:
    print(f'Tu angulo {angulo} no esta en el rango de 0 a 360, por lo tanto es INVALIDO')
else:
    if angulo < 90:
        print(f'El angulo de {angulo} grados es un angulo AGUDO')
    elif angulo == 90:
        print(f'El angulo de {angulo} grados es un angulo RECTO')
    elif angulo < 180:
        print(f'El angulo de {angulo} grados es un angulo OBTUSO')
    elif angulo == 180:
        print(f'El angulo de {angulo} grados es un angulo LLANO')
    elif angulo < 360:
        print(f'El angulo de {angulo} grados es un angulo CONCAVO')
    else:
        print(f'El angulo de {angulo} grados es un angulo COMPLETO O CERRADO')
        
        
print('\nProceso terminado')



