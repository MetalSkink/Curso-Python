'''
Bucles - Ejercicio 4:
Hacer un programa para sumar números pares dentro de un rango.
'''
sumapares = []
acum= 0
a = int(input("Digite de donde voy a empezar a sumar: "))
b = int(input("Digite hasta donde quiere sumar: "))

for i in range (a,b+1):
    if (i % 2 == 0):
        sumapares.append(i)

for i in range(0, len(sumapares)):
     acum +=  sumapares[i]

print(f"El aumuludado fue {acum}")

