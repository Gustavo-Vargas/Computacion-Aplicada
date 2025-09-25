# p040-multiplos-continue.py
# Imprime solo los multiplos de 10 hasta el 200

print('\033[2J\033[H')
print('Buscando múltiplos de 10 entre 1 y 200 ...')

c = 10

while c <= 200:
    c += 1
    if c % 10 != 0:
        continue # ignora todo lo que sigue y salta a la siguiente iteracion
    # SOlo se ejecuta si el numero es multiplo de 10
    print(f'{c}', end='')
    
print('\n Busqueda terminada ...')




