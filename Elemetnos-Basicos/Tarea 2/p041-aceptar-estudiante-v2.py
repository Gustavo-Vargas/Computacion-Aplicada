# p041-aceptar-estudiante-v2.py
# Problema: La "Universidad Kitty Kat SA" solo acepta estudiantes que cumplan con los siguientes requisitos: ser
# mujer, ser mayor de 21 años y tener un promedio entre 8 y 9.5.
# Escribe un programa que solicite el nombre, sexo (h/m), edad y tres calificaciones de un aspirante. El programa
# debe evaluar los datos y mostrar un mensaje claro que indique si el estudiante fue aceptado. Si no es aceptado, el
# mensaje debe especificar la razón del rechazo (ya sea por no cumplir con el sexo, la edad o el promedio
# requerido).
# Ejemplos de ejecución:
# • Entrada: Nombre: Maria, Sexo: m, Edad: 22, Calificaciones: 10, 9, 8.5
# • Salida: ¡Felicidades, Maria! Has sido aceptada. Cumples con la edad y tu promedio de 9.17 está dentro del
# rango permitido.
# • Entrada: Nombre: Jose, Sexo: h, Edad: 21, Calificaciones: 7, 6, 5
# • Salida: Lo sentimos, Jose. La universidad solo acepta mujeres.
# • Entrada: Nombre: Dolores, Sexo: m, Edad: 20, Calificaciones: 10, 10, 10
# • Salida: Lo sentimos, Dolores. No cumples con la edad requerida (mayores de 21 años).
# • Entrada: Nombre: Sandra, Sexo: m, Edad: 25, Calificaciones: 7, 6, 5
# • Salida: Lo sentimos, Sandra. Tu promedio de 6.0 no alcanza el mínimo requerido de 8.

print('\033[2J\033[H')
print('--- Verificar estudiante ---')

nombre = input('Dame tu nombre: ')
sexo = input('Dame tu sexo [f/m]: ').lower()
edad = int(input('Dame tu edad: '))

print('Ingresa tus calificaciones por espacios:')
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3 = float(cal1), float(cal2), float(cal3)

promedio = (cal1 + cal2 + cal3) / 3

if sexo == 'f':
    if edad > 21: 
        if promedio >= 8 and promedio <= 9.5:
            print(f'¡Felicidades, {nombre}! Has sido aceptada. Cumples con la edad y tu promedio de {promedio:.2f} está dentro del rango permitido.')
        else:
            print(f'Lo sentimos, {nombre}. Tu promedio de {promedio:.2f} no alcanza el mínimo requerido de 8.')
    else:
        print(f'Lo sentimos, {nombre}. No cumples con la edad requerida (mayores de 21 años).')
else:
    print(f'Lo sentimos, {nombre}. La universidad solo acepta mujeres.')

print('\nProceso temrinado ...')


