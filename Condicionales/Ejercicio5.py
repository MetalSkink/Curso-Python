'''
Ejercicio 5: 
Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menú de opciones: 
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
'''

saldo = 1000

print("\t.:MENU:.")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero en la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion = float(input("Digite una opcion de menu: "))

print()

if opcion == 1:
    nuevo = float(input("Cuanto quiere ingresar -> "))
    print(f"Nuevo saldo: {saldo+nuevo}")
elif opcion == 2:
    retiro = float(input("Cuanto quiere retirar -> "))
    if retiro > saldo:
        print("No tiene saldo suficiente para retirar")
    else: 
        print(f"Nuevo saldo: {saldo-retiro}")
elif opcion == 3:
    print(f"Saldo disponible: {saldo}")
elif opcion == 4:
    print(f"Hasta luego :D")
else: 
    print(f"Operacion no valida")