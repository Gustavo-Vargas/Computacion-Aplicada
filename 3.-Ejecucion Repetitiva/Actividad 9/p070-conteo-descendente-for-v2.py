# p070-conteo-descendente-for-v2.py
# Imprime lso numero de n a 1, en docremetos de m, usando un ciclo for


print('\033[2J\033[H')
print("--- Iniciando Secuencia ascendente ---")

n = int(input('Desde donde? '))
m = int(input('De cuatno en cuanto? '))

for f in range(n,0,-m):
    print(f, end='')

