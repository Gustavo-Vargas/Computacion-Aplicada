# p026–convertir-temperaturas-v2.py
# Convertir temperatiras de grados celcius a farenheit y viceversa

print('\033[2J\033[H')
print('\033[1mConvertir de Grados Celcius a grados Farenheit\033[0m')

print('\033[34m')
print('[C] Celcius a Farenheit')
print('[F] Farenheit a Celcius')
print('\033[0m')
op = input('Elige ? ').upper()

if op == 'C':
    print('\nConvirtiendo de Celcius a Farenheit')
    c = float(input('Introduce los grados Celcius : '))
    f = ( c * 9 / 5) + 32
    print('\n{c:.2f} Grados Celcius, equivale a {f::.2f} grados Centigrados')
else:
    if op == 'F':
        print('\nConvirtiendo de Farenheit a Celcius')
        c = float(input('Introduce los grados Farenheit : '))
        f = ( f - 32) * 5 / 9
        print('\n{f:.2f} Grados Farenheit, equivale a {c::.2f} grados Centigrados')
    else:
        print('✖️ OPCION INVALIDA')

