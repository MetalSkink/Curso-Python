'''
Bucles - Ejercicio 9:
Hacer un programa donde el usuario ingrese una frase, se le devolverá la misma frase 
pero sin espacios en blanco y además un contador de cuántos 
caracteres tiene la frase (sin contar los espacios en blanco).
'''

frase = input("Inserte una frase -> ")
contador=0

for i in frase:
    if i != " ":
        print(i,end="")
        contador += 1
print(f"\nTu palabra tiene {contador} letras")