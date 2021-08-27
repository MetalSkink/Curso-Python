'''
Bucles - Ejercicio 1:
Llenar una lista con los números del 1 al 50, luego mostrar la lista con un bucle for, los elementos deben mostrarse de la siguiente forma:
1 - 2 - 3 - 4 - 5 - … - 50
'''

lista  = []
lista2 = list(range(1,51))

for i in range(1,51):
    lista.append(i)

for i in lista:
    if i == 50:
        print(i)
        break
    print(i,end=" - ")