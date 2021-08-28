# Cadenas - Ejercicio 5:
# Hacer un programa donde se cuente cada una de las vocales en una cadena,
# mostrar el conteo de las apariciones de cada vocal.

word = input("Ingresa una frase -> ").upper()

print(f"\nNumero de apariciones de 'a': {word.count('A')}")
print(f"Numero de apariciones de 'e': {word.count('E')}")
print(f"Numero de apariciones de 'i': {word.count('I')}")
print(f"Numero de apariciones de 'o': {word.count('O')}")
print(f"Numero de apariciones de 'u': {word.count('U')}")