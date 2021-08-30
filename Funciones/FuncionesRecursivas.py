# Funciones Recursivas

def cuentaRegresiva(num):
    if num > 0: #Caso iterativo
        print(num)
        cuentaRegresiva(num-1)
    else: #Caso base
        print("BOOM!")

cuentaRegresiva(10)