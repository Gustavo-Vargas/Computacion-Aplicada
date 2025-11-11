# p129-func-param-nombre.py

print('\033[H\033[J')

# Declaracion
def saluda(apaterno:str, amaterno:str, nombre:str, edad:int) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}, tienes {edad} años de edad.... ')
    print()
    
# llamado
saluda('castaneda', 'ramirez', 'carlos hector', '25')
saluda(edad=32,nombre='Rocio',amaterno='Bernal',apaterno='Soto')
saluda(nombre='Juan', apaterno='Diaz',edad=18,amaterno='Lopez')
