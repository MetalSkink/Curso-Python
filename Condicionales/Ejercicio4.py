'''
Condicionales - Ejercicio 4: 
Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritméticas básicas (suma, resta, multiplicación y división). 
El usuario debe especificar la operación con el primer carácter  del nombre de la operación.
S, s – Suma
R, r – Resta
P, p, M, m – Multiplicación
D, d - División
'''
a = float(input("num1 -> "))
b = float(input("num2 -> "))

print("¿Que tipo de operacion quieres hacer?")
print("s - Suma ")
print("r - Resta ")
print("m - Multiplicacion")
print("d - Division")

tipo = input("-> ").lower()


if tipo == 's':
    print(f"El resultado de la suma es {a+b:.2f}")
elif tipo == 'r':
    print(f"El resultado de la resta es {a-b:.2f}")
elif tipo == 'm' or tipo == 'p':
    print(f"El resultado de la multiplicacion es {a*b:.2f}")
elif tipo == 'd':
    print(f"El resultado de la division es {a/b:.2f}")
else:
    print(f"El caracter '{tipo}' no corresponde a ninguna operacion")
