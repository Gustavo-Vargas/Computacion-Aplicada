#  p027-calcular-paga-extra.py
# Calcula la paga de un trbajador considerando la shoras extra (se pagan al doble)

print('\033[2J\033[H')
print('Calculadno la paga extra d eun trabajador')

# Entrada
print('Introduce los datos del trabajador')
nombre = input('Nombre ? ')
horas = int(input('Horas trabajadas ? '))
paga_hora = float(input('Paga por hora ? '))

# Proceso
horas_normales = 40
horas_extra = 0
paga_normal = 0
pago_extra = 0
total = 0

if horas <= horas_normales:
    paga_normal = horas * paga_hora
    total = paga_normal
else:
    paga_normal = horas_normales * paga_hora
    horas_extra = horas - horas_normales
    pago_extra = horas_extra * ( paga_hora * 2)
    total = paga_normal + pago_extra

print('\nCalculo completo ')
print(f'{nombre} trabajo {horas} horas. a una paga de {paga_hora} pesos por hora, horas extra {horas_extra}')
print(f'Paga normal     : $ {paga_normal:13,.2f}')
print(f'Paga extra      : $ {pago_extra:13,.2f}')
print(f'Total a pagar   : $ {total:13,.2f}')
