# p132-funcion-retorno.py
# FUncion que regresa valores

print('\033[H\033[J')

def suma(n1:float, n2:float, n3:float) -> float:
    return n1 + n2 + n3


suma_resultado = suma(100,200,300)
print(f'La suma es : {suma_resultado}')

print('Dame tres numeros flotantes separados enter: ')
a, b,c = float(input()), float(input()), float(input())
print(f'La suma de los nuemros es {suma(a,b,c):,.2f}')
    
