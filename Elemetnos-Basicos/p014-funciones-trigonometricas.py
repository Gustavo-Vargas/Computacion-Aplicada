# p014-funciones-trigonometricas.py
# Demostrar el uso de funcioones trigonometricas

import math as mt

angulo = 45
radiantes = mt.radians(angulo) # Convertir grados a radianes

# Calcular las funciones trigonometricas

seno = mt.sin(radiantes)
coseno = mt.cos(radiantes)
tangente = mt.tan(radiantes)

grados = mt.degrees(radiantes) # Convertir radianes a grados

# Formatear salida con f-string precio a la impresion 
salida = ( 'Resumen de funciones \n'
 f'El seno es    : {seno:.4f} \n'
 f'El coseno es  : {coseno:.4f} \n'
 f'La tangente es: {tangente:.4f} \n'
 f'El angulo {angulo} grados, equivale a {radiantes:.4f} radianes \n'
 f'Los {radiantes:.4f} radianes, equivale a {grados:.4f} grados' 
)

# Mostrar familia formateada
print(salida)

