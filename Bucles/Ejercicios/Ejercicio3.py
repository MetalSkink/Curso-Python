'''
Bucles - Ejercicio 3:
Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor
'''

lista = []

ban = False

while ban == False:
    num = int(input("Dame un numero o pulsa 0 para salir -> "))
    if num == 0:
        break
    lista.append(num)

if len(lista) == 0:
    print("Tu lista esta vacia :(")
else:
    lista.sort()
    print(lista)
