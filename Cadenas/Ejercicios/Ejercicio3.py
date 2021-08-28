# Cadenas - Ejercicio 3:
# Hacer un programa que determine si una palabra o frase es palíndroma. 
# Una cadena palíndroma se lee igual de izquierda a derecha que de derecha a izquierda.

word1 = input("Ingresa una frase -> ").replace(' ','')

word2 = word1[::-1]

if word1 == word2: 
    print("Es palindromo")
else: 
    print("No es palindromo")