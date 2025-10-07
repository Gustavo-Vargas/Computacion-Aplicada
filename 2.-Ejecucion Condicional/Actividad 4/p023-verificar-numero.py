#p023-verificar-numero.py
# Verifica si un nuemor es positivo, negativo o cero

print('Verificando si un numero es positivo, negativo o cero')

# Entrada
print('Dame un numero entero?')
numero = int(input())

# Proceso 
if numero > 0:
    print('El numero es POSITIVO 👍')

if numero < 0:
    print('El numero es NEGATIVO 👎')

if numero == 0:
    print('El numero es CERO 🤷‍♂️')

print('\nProceso Terminado')