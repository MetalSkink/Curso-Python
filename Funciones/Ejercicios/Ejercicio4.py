# Funciones - Ejercicio 4:
# Desarrollar un programa para calcular el factorial 
# de un número con ayuda de una función recursiva.

def calcularFactorial(num):
    if num > 0:
        acum = num * calcularFactorial(num-1)
    else:
        acum = 1
    return acum 

number = int(input("Dame el numero del que quieres el factorial -> "))

print(f"El factorial de {number} es {calcularFactorial(number)}")