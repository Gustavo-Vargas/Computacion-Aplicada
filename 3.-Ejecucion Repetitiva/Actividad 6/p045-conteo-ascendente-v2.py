# p037-conteo-ascendente-v2.py
# IMprime los numeros de  1 a 100 un ciclo while

print('\033[2J\033[H')
print('Iniciando secuecnia ascendente ...')

n = int(input('Hasta donde ? '))
m = int(input('De cuanto en cuatno ?'))

c = 1

while c <= n:
    print(f' {c}', end='')
    c += m

print('\n Secuecnia Completada')

