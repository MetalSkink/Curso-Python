'''
Cadenas - Ejercicio 1:
Hacer un programa donde se deberá imprimir por la consola la palabra con más caracteres de dos palabras dadas. 
En el caso de que ambas palabras tengan la misma cantidad de caracteres,
deberás mostrar el mensaje "Son iguales".
'''

word1 = input("Dame una palabra -> ")
word2 = input("Dame una segunda palabra -> ")

if len(word1) == len(word2):
    print("Las palabras tienen la misma cantidad de letras")
elif len(word1) > len(word2):
    print(f"Las palalabra {word1} tiene mas letras que {word2}")
else:
    print(f"Las palalabra {word2} tiene mas letras que {word1}")
 