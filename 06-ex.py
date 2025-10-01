# problema: [-12938,2356,1293,298091,38372,18375,28301,-2938,53, -98235, 286356, 08341, 93845]
# detectar el menor y el mayor de todos

# list = [-12938,2356,1293,298091,38372,18375,28301,-2938,53, -98235, 286356, 8341, 93845]
# print(max(list))
# print(min(list))

min = 999999
max = -999999

lista = [-12938,2356,1293,298091,38372,18375,28301,-2938,53, -98235, 286356, 0.8341, 93845]

for var in lista:
    if (var > max):
        max = var
    
    if (var < min):
        min = var
    
print("el valor mínimo es:", min)
print("el valor máximo es:", max)