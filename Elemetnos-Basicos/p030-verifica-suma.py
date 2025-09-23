# p030-verifica-suma.py
# Verificar si la suma de dos nuemor es igual a un tercero
# 


print('\033[2J\033[H')
print('---- Verificar si la suma de dos nuemros es  igual a un tercero ')

# Entrada 
print('Dame 3 nuemros enteros separados por un esapcio : ')
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

# Proceso
if n1+n2 == n3:
    print(f' {n1} + {n2} = {n3} !')
elif n1+n3 == n2:
    print(f' {n1} + {n3} = {n2} !')
elif n2+n3 == n1:
    print(f' {n2} + {n3} = {n1} !')
elif n1 == n2 == n3:
    print(f' {n1}, {n2}, {n1} son IGUALES !')
elif n1 != n2 != n3:
    print(f' {n1}, {n2}, {n1} son todos DIFERENTES !')
else :
    print(f' Es posible qeu {n1}, {n2}, {n1} sea un par igual !')

print('\nProceso temrinado')


