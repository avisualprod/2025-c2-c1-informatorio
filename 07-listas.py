# orden      0  1  2  3  4 5 6 7 8 9 10 11 12 13 14
# lista = [1002,32,12,32,1,2,3,4,5,6,7,8,9,0,10]

# print(lista)

# print (max(lista))

# Validar si en la siguiente lista existen dos números
# contiguos que su suma de el valor target

#posic   0    1    2   3   4  5  6  7  8  9 10 11 12 13 14 15
# lista = [5, 1002, 32, 12, 32, 7, 1, 2, 3, 4, 6, 7, 8, 9, 0, 10]
# target = 12

# posiciones = len(lista) - 1

# for pos in range(0, posiciones):
#     suma = lista[pos] + lista[pos + 1]
#     if (suma == target):
#         cumple = True
#         print("El valor de la posición:", pos, "y la posición", pos + 1, "dan igual al target (", target,")")
#         break

# if (not cumple):
#     print("ninguno de los valores suman lo del target")

# cumple = False
# for pos in range(0, posiciones):
#     for prx in range(pos + 1, posiciones):
#         suma = lista[pos] + lista[prx]
#         if (suma == target):
#             cumple = True
#             print("El valor de la posición:", pos, "y la posición", pos + 1, "dan igual al target")
            
# if (not cumple):
#     print("ninguno de los valores suman lo del target")

lista = [1002,32,12,32,1,2,3,4,5,6,7,8,9,0,10,2]
target = 12

cumple = False  #0,15
for i in range(0,len(lista)-1):
        for j in range(i+1, len(lista)):
              if((lista[i] + lista[j] == 12)):
                    print(f"Mi numero en la posicion {i}({lista[i]}) y mi numero en la posicion {j}({lista[j]}) es igual a 12") 