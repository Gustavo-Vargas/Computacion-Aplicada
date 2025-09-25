# 039-conteo-descendente-v2.py
# Impriem los numeros de n a 1, usando un ciclo while

print('\033[2J\033[H')
print('Iniciando secuecnia ascendente ...')

n = int(input('Desde donde? '))
m = int(input('De cuanto en cuatno ? '))

c = n

while c >= 1:
    print(f'{c}', end='')
    c -= m
    
print('\n Terminado .')

