'''
Bucles - Ejercicio 10:
Hacer un programa que pida una cadena por teclado, 
luego meta los caracteres en una lista sin repetir caracteres.
'''

frase = input("Inserte una frase -> ")
lista = []

for i in frase:
    if not i in lista:
        lista.append(i)
print(lista)    