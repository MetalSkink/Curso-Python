'''
Cadenas - Ejercicio 2:
Hacer un programa para detectar si una frase introducida por el usuario finaliza con un punto "." o no. 
Deberás imprimir por la consola una de las siguientes opciones; 
"Termina con un punto" o por el contrario "No termina con un punto".
'''

word = input("Ingresa una frase -> ")

if word.endswith('.'):
    print("Termina con un punto")
else:
    print("No termina con un punto")