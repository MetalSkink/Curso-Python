'''
Ejercicio2 :
Hacer un programa que pida 3 numeros y determina cual
es mayor
'''

a = float(input("a -> "))
b = float(input("b -> "))
c = float(input("c -> "))

if a == b and b == c:
    print("Los 3 numeros son iguales")
if a == b and b > c:
    print("Los primeros 2 numero son mayores e iguales")
if b == c and b > a:
    print("El segundo y tercer numero son mayores e iguales")
if a == c and a > b:
    print("El primer y tercer numero son mayores e iguales")
if a == b and b == c:
    print("Los 3 numeros son iguales")
elif a>b and a>c:
    print(f"{a} es el numero mayor")
elif b>a and b>c:
    print(f"{b} es el numero mayor")
elif c>a and c>b:
    print(f"{c} es el numero mayor")