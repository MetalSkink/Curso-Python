# Listas

lista = ["Lunes", "Martes", "Miercoles", 40, 68.76, 40, [1,2,3], True]
# lista = ["Lunes", "Martes", "Miercoles", 40, 68.76, 40, [1,2,3], True] * 3

print(lista)
print(lista[0])
print(lista[-4])
print(lista[0:3])
print(lista[:4])
print(lista[2:])

print(len(lista))
lista.append("elemento extra")
lista.insert(2,"Mimimimieercoles")
lista.extend([False, "sombrero"])
lista3 = lista + ["botas", "pistola"]
print("Martes" in lista)
print(lista.index(40))
print(lista.count(40))
lista.pop(3)
lista.remove(40)
print(lista3)
print(lista)
lista.reverse()
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
lista.clear()
print(lista)