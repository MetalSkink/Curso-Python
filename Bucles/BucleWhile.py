# Bucle while

import math

numero = int(input("Digite un numero -> "))

while numero<0:
    print("ERROR: Ingrese un numero positivo")
    numero = int(input("Digite un numero -> "))

print(f"\nSu raiz cuadrada es {(math.sqrt(numero)):.2f}")

i = 0

while i < 10:
    print(f"Hola mundo por vez numero {i}")
    i += 1