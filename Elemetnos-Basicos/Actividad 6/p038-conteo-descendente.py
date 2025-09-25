# p038-conteo-descendente.py
# Impriem los numeros de 100 a 1, usando un ciclo while

print('\033[2J\033[H')
print('Iniciando secuecnia ascendente ...')

c = 100

while c >= 1:
    print(f'{c}', end='')
    c -= 1
    
print('\n Terminado')

