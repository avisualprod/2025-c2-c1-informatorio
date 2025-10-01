# Determinar si el usuario, el cual
# ingresa por pantalla si anho de nacimiento
# es mayor o menos de edad

# anho_usuario = int(input('Ingrese su año de nacimiento: '))
# anho_actual = 2025

# edad = anho_actual - anho_usuario

# mayor_edad = int(input('A qué edad es la mayoría de edad? '))

# if(edad >= mayor_edad):
#     print('El usuario tiene mayoría de edad')
# else:
#     print('El usuario es menor de edad')

import datetime

fechanac_usuario = str(input('Ingrese su fecha de nacimiento (día-mes-año):'))
fecha_actual = datetime.datetime.today().date()
fecha_actualformat = fecha_actual.strftime('%d-%m-%Y')
fecha_hoy = datetime.datetime.strptime(fecha_actualformat,'%d-%m-%Y').date()
Nac_usuario = datetime.datetime.strptime(fechanac_usuario,'%d-%m-%Y').date()

edad = fecha_hoy.year - Nac_usuario.year

if (fecha_hoy.day, fecha_hoy.month) < (Nac_usuario.day, Nac_usuario.month):
    edad -= 1

if edad >= 18:
    print('El usuario tiene mayoría de edad')
else:
    print('El usuario es menor de edad')

# if edad >= 18
#     print('Usuario mayor de edad')
# else
#     print('Usuario menor de edad')
