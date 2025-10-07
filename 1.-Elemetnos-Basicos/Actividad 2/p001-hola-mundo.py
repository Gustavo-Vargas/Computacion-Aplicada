# p001-hola-mundo.py
# Lee datos y envia un saludo

print("leyendo datos y enviando un saludo: \n")

nombre = input("Dame tu nombre: ")
edad = int( input("Dame tu Edad: "))
peso = float( input("Dame tu eso: "))
cansado = True

print(f"{nombre} bienvenido a python, tu edad es {edad}, tu peso es {peso}")

print( type(nombre) )
print( type(edad) )
print( type(peso) )
print( type(cansado) )
