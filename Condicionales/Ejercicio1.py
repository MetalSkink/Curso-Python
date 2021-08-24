'''
Ejercicio 1:
Hacer un programa que pida 2 numero y se de cuanta cual de ellos es par o si ambos lo son
'''

a = float(input("a -> "))
b = float(input("b -> "))

if a%2 == 0 and b%2 == 0:
    print("Ambos numeros son pares")
elif a%2 == 0:
    print("El primer numero es par")
elif b%2 == 0:
    print("El segundo numero es par")
else:
    print("Ningun numero es par")