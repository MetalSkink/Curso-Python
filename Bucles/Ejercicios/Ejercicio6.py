'''
Hacer un programa que pida un número por teclado y guarde en una lista su tabla de multiplicar 
hasta el 10. Por ejemplo, si digita el 5 la lista tendrá:
5, 10, 15, 20, 25, 30, 35, 40, 45, 50
'''
numero = int(input("\nDame un numero positivo -> "))
lista = []

# for i in range(10):
#     acum += numero
#     lista.append(acum)
#     print(lista[i],end=", ")

for i in range(1,11):
    lista.append(numero*i)
    print(lista[i-1],end=", ")