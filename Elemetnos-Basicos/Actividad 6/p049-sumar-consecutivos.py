# p041-sumar-consecutivos.py
# Suma numeros consecutivos hasta alcanzar 100

print('\033[2J\033[H')
print('Rifa ...')

c = 0
suma = 0
meta = 15000

while c <= 200:
    c += 1
    suma += c
    print(f'{c}', end='')
    
    if suma >= meta:
        print('\n\n Meta alcanzada')
        print(f'Boletos: {c}')
        break
    
print('\n \nProceso temrinado ...')









