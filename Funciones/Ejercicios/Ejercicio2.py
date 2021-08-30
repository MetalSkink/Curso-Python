# Funciones - Ejercicio 2:
# Hacer un programa que pida la anchura y altura de un rectángulo 
# y con ayuda de una función lo dibuje con *.

def dibuja_rectangulo(anch,alto):
    for j in range(alto):
        for i in range(anch):
            print("*",end=" ")
        print()

anch = int(input("Dame el ancho del rectangulo -> "))
alto = int(input("Dame el alto del rectangulo -> "))

dibuja_rectangulo(anch,alto)