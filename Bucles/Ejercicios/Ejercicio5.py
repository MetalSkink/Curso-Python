'''
Bucles - Ejercicio 5:
Hacer un programa para calcular el factorial de un número positivo.
'''
numero = int(input("\nDame un numero positivo -> "))

while numero<0:
    print("ERROR-El numero debe ser positivo")
    numero = int(input("\nDame un numero positivo -> "))
    
resultado = 1

for i in range(1, numero+1):
    resultado *= i

print(f"El factorial de {numero} es {resultado} ")