# p003-area-triangulo.py
# Calcula el area de un triangulo

print('Calculando el area de un traingulo \n')

# Entrada
print('Dame la base y la altura separados por Enter: ')
base, altura = int( input()), int( input() ) # lee dos valores

# Proceso
area = (base * altura) / 2

# Salida 
print('El triangulo de base: ', base)
print('El triangulo de altura: ', altura)
print('El triangulo de area: ', area)

print(f'\nEl triangulo de base {base} y altura {altura} tiene un area de {area:,.2f}')

print('EL triangulo de base ' + str(base) + ' y altura ' + str(altura) + ' tiene un area de ' + str(area) )
