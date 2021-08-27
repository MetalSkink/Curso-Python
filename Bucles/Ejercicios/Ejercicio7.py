'''
Bucles - Ejercicio 7:
Realizar un juego para adivinar un número. Para ello generar un número aleatorio entre 0-100, y luego ir pidiendo números
indicando “es mayor” o “es menor” según sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta 
y mostrar el número de intentos.
'''
import random

aleatorio = random.randint(0,100)

contador = 0

while True:
    numero = int(input("Traté de adivinar el numero entre 1 y 100 -> "))
    contador += 1
    if numero == aleatorio:
        print("\nFELICIDADES HAS GANADO")
        print(f"Numero de intentos {contador}")
        break
    elif aleatorio>numero:
        print("El numero es mas alto")
    elif aleatorio<numero:
        print("El numero es mas bajo")