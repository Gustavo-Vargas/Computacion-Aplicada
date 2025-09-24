# p019-calculo-tiempo
# Diseña un programa que tome una cantidad de horas como un número entero. El programa debe calcular y mostrar
# el equivalente de ese tiempo en:
# • Días (considerando que 1 día tiene 24 horas)
# • Minutos (considerando que 1 hora tiene 60 minutos)
# • Segundos (considerando que 1 minuto tiene 60 segundos)

print("-" * 40)
print('Calcular equivalencia de tiempo')
print("-" * 40)

# Entrada
horas = int(input('Ingrese la cantidad de horas: '))

# Proceso
dias = horas // 24
minutos = horas * 60
segundo = minutos * 60

# Salida
print("-" * 40)
print(f'Equivalente en días: {dias} días')
print(f'Equivalente en minutos: {minutos} minutos')
print(f'Equivalente en segundos: {segundo} segundos')
print("-" * 40)
