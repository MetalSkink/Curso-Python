# Funciones sin retorno de valor

def saludar(nombre):
    print(f"Hello {nombre}")

saludar("Xavier")
saludar("Salma")

def tabla_multiplicar(num):
    print()
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

tabla_multiplicar(7)
tabla_multiplicar(9)
tabla_multiplicar(14)