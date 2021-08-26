'''
Colecciones - Ejercicio 2:
Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe haber repeticiones):

- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas.
'''

listA = [1,2,3,4,5,4,3,2,2,1,5]
listB = [4,5,6,7,8,4,5,6,7,7,8]

listA = set(listA)
listB = set(listB)

list1 = list(listA | listB)
list2 = list(listA - listB)
list3 = list(listB - listA)
list4 = list(listA & listB)

print(f"Lista 1 -> {list1}")
print(f"Lista 2 -> {list2}")
print(f"Lista 3 -> {list3}")
print(f"Lista 4 -> {list4}")
