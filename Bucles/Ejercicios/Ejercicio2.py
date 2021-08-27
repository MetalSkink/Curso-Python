'''
Bucles - Ejercicio 2:
Llenar una lista con los números del 1 al 10, luego modificar los elementos de la lista multiplicándolos por un valor que el usuario digite.
'''

lista = list(range(1,11))
num = int(input("Por que valor los quieres multiplicar -> "))

# for i in range(0, len(lista)):
#     lista[i] *= num

for indice,i in enumerate(lista):
    lista[indice] *= num

print(f"\nLista multiplicada por el numero: {num} \n{lista}" )

