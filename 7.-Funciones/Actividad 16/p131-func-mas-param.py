# p131-func-mas-param.py

print('\033[H\033[J')


def saluda_todos(*todos:str) -> None:
    print('Saluda a todos: ')
    for nombre in todos:
        print(f'Saludos a {nombre}')
    print()

saluda_todos('Carlos')
saluda_todos('Carlos','Jose','Luis')
saluda_todos('a','b','c','d','e','f')
