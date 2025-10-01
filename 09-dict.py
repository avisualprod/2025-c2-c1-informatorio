# en función del nombre del mes, quiero que me diga 
# a qué número corresponde 
# por ej. agosto --> 8

meses = {'enero' : 1,
         'febrero' : 2,
         'marzo' : 3,
         'abril' : 4,
         'mayo' : 5,
         'junio' : 6,
         'juio' : 7,
         'agosto' : 8,
         'septiembre' : 9,
         'octubre' : 10,
         'noviembre' : 11,
         'diciembre' : 12}

mes_busc = input('Ingrese el mes buscado, escrito en minúsculas: ').lower()

print(f'El mes que digitó es el número: {meses[mes_busc]}')

invertir_claves = {value: key for key, value in meses.items()}

print(invertir_claves)
