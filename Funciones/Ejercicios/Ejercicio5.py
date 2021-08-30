# Funciones - Ejercicio 5:
# Desarrollar un programa que permita sumar los dígitos
# de un número con ayuda de una función recursiva.

def sumaDigitos(num):
    if num == 0: 
        acum = 0
    else:
        acum = sumaDigitos(num//10) + (num%10)
    return acum


valor = int(input("Dame el numero -> "))
print(f"La suma de los digitos de {valor} es igual a {sumaDigitos(valor)}")