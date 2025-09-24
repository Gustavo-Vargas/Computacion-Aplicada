# p010-operaciones-matematicas.py
# Demostrar el uso de los difeentes operadores aritmeticos con numeros

print("="*80)
print('Calculadora d eoperaciones Matematicas ')
print("="*80)

# Entrada 
x = float(input('Valor de x ? '))#3 #2.5 #100.35045
y = float(input('Valor de y ? ')) #2 #2 #20.343

# Salida 
print(f'Suma          : {x:>6.2f} + {y:<6.2f} = {x + y :>15.2f} ')
print(f'Resta         : {x:>6.2f} - {y:<6.2f} = {x - y :>15.2f} ')
print(f'Multiplicacion: {x:>6.2f} * {y:<6.2f} = {x * y :>15.2f} ')
print(f'Division      : {x:>6.2f} / {y:<6.2f} = {x / y :>15.2f} ')
print(f'Modulo        : {x:>6.2f} % {y:<6.2f} = {x % y :>15.2f} ')
print(f'Div. Entera   : {x:>6.2f} // {y:<6.2f} = {x // y :>15.2f} ')
print("="*80)
