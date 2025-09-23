# p031-2da-ley-de-newton.py
# Calcular la segunda ley de newton
# Fuerza = masa * aceleracion, masa = fuerza / aceleracion, aceleracion = fuerza / masa

print('\033[2J\033[H')
print('Calcular los valores de la segunda ley de newton')
print('[F ]uerza       =masa * aceleracion')
print('[M ]asa         =fuerza / aceleracion')
print('[A ]celeracion  =fuerza / masa')
opcion = input('Elije una opcion ? ').upper()

if opcion == 'F':
    print('\nCalculadno la Fuerza')
    masa = float(input('Masa ? '))
    aceleracion = float(input('Aceleracion ? '))
    fuerza = masa * aceleracion
    print(f'\nLa fuerza es: {fuerza} ')
elif opcion == 'M':
    print('\nCalculadno la Masa')
    fuerza = float(input('Fuerza ? '))
    aceleracion = float(input('Aceleracion ? '))
    masa = fuerza / aceleracion
    print(f'\nLa Masa es: {masa} ')
elif opcion == 'A':
    print('\nCalculadno la Aceleracion')
    fuerza = float(input('Fuerza ? '))
    masa = float(input('Masa ? '))
    aceleracion = fuerza / masa
    print(f'\nLa Aceleracion es: {aceleracion} ')
else:
    print('\nOpcion invalida, elige F, M o A')
    

print('\nProceso temrinado')


