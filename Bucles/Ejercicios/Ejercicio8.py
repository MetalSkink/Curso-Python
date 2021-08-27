'''
Bucles - Ejercicio 8:
Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menú de opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
'''
saldo = 1000

while True:
    print("\n\t.:MENU:.",
          "¿Que operacion quiere realizar",
          "1. Ingresar dinero en la cuenta",
          "2. Retirar dinero de la cuenta",
          "3. Mostrar dinero disponible",
          "4. Salir",sep="\n")
    operacion = int(input("-> "))

    if operacion == 1:
        ingreso = float(input("Cuanto va a ingresar "))
        saldo += ingreso
    elif operacion == 2:
        retiro = float(input("Cuanto va a retirar "))
        if saldo < retiro:
            print("No tiene saldo suficiente")
        else:
            saldo -= retiro
            print(f"Retiro con exito {retiro}")
    elif operacion == 3:
        print(f"Su saldo disponible es {saldo}")
    elif operacion == 4:
        print("Hasta luego que pase buena tarde :D")
        break