# p042-conteo-numeros.py
# Permite ingresar n numeros, se detiene al introducir 999, y meustra estadisticas 

print('\033[2J\033[H')
print('Rifa ...')

cuenta = 0
suma = 0
cp = cn = cz = 0

while True:
    num = int(input('Introduce un número entero? '))
    if num == 999:
        print('Detectando sentinela 999, me voy ...')
        break
    cuenta += 1
    suma += num
    if num > 0 : cp+=1
    elif num < 0 : cn+=1
    else: cz +=1

    
print('\n------------- RESUMEN FINAL --------------')
print(f'Numero encotnrados: {cuenta}')
print(f'La suma total fue {suma}')
print(f'Positivos: {cp}')
print(f'Negativos: {cn}')
print(f'Ceros: {cz}')


