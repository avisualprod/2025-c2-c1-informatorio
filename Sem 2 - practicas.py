# Ejercicio 1: Calcular la suma de los números del 1 al 100.

print('----------> Ejercicio 1:')

cont = 0

for suma in range(cont + 1, 101):
    cont += suma


print('La suma de todos los números del 1 al 100 da:',cont)

# Ejercicio 2: Mostrar los números pares del 1 al 50.

print('----------> Ejercicio 2:')

for numeros in range(1,51):
    if numeros % 2 == 0:
        print (numeros)


# Ejercicio 3: Calcular área de un triángulo

print('----------> Ejercicio 3:')

base_tr = int(input('Ingrese el valor de la Base del triángulo (en cm): '))

altura_tr = int(input('Ingrese el valor de la Altura del triángulo (en cm): '))

area_tr = (base_tr * altura_tr) / 2

print('El Área del triángulo es:', area_tr, 'centímetros')


#Ejercicio 4: Validación de contraseña - Guardar una contraseña definida en el código. El usuario tiene 3 intentos para ingresarla correctamente. Si falla, mostrar “Cuenta bloqueada”.

print('----------> Ejercicio 4:')

passwrd = "Info1234"

intentos= 0

max_intentos = 3

while intentos < max_intentos:
    pass_usr = input('Ingrese su contraseña: ')
    if pass_usr == passwrd:
        print ('Contraseña correcta. Acceso otorgado')
    else:
        intentos += 1
    

print('Cuenta bloqueada.')


# Ejercicio 5: Factorial - Pedir un número y calcular su factorial (ej: 5! = 5×4×3×2×1). 

print('----------> Ejercicio 5:')

numer_fac = int(input('Ingrese un número: '))

for fac in range(numer_fac - 1, 0, -1):
    print(fac)

for factorial in range(numer_fac - 1, 0, -1):
    numer_fac *= factorial

print('Su factorial es:', numer_fac)
