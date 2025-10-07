# p006-conversor-temperatura.py
# Convierte de grados Celsius a Fahrenheit

print('Conversor de Teperatura ( Celcius - Fahrenheit ) \n')

celcius = float ( input('Ingresa la tenperatura en Celcius : ' ))

farenheit = ( celcius * 9 / 5 ) + 32

print(f'\n{celcius:.2f} Grados Celcius equivale a {farenheit:.2f} Grados Farenheit' )
