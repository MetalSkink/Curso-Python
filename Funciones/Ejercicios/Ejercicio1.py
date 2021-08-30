# Funciones - Ejercicio 1:
# Desarrollar un programa que pueda calcular el valor del tipo de cambio de moneda 
# (de tu moneda – hacia dólar y viceversa).

def dolar_pesos():
    num = float(input("Dame tus dolares -> "))
    print(f"{num} dolares son {num*20.20:.2f} pesos")

def peso_dolar():
    num = float(input("Dame tus pesos -> "))
    print(f"{num} pesos son {num/20.20:.2f} dolares")

while True:
    print("\n\t.:MENU:.",
          "1.- Convertir de peso a dolares",
          "2.- Convertir de dolar a peso",
          "3.- Salir",sep="\n")
    operacion = int(input("-> "))
    if operacion == 1:
        dolar_pesos()
    elif operacion == 2:
        peso_dolar()
    elif operacion == 3:
        break
    else:
        print("Operacion no permitida, intente otra vez")