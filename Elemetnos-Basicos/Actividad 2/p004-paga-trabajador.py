# p004-paga-trabajador.py
# Calcula la paga de un trabajador

print('Calculando la paga de un trbajador \n')

# Entrada
nombre = input('Nombre del trabajador: ')
horas = int( input('Horas: '))
paga = float( input('Paga x Hora: '))

# Proceso
tasa = 0.03 # inpuesto de hacienda
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

# Salida
print('\nResumen de pagos ')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga:.2f} pesos, con una tasa de {tasa:.2%}')
print(f'Paga Bruta    : {pagabruta:,.2f} ')
print(f'Impuesto      : {impuesto:,.2f} ')
print(f'Paga Neta     : {paganeta:,.2f} ')
