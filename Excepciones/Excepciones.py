# Excepciones
while True:
    try:
        numero = int(input("Digite un numero: "))
        print(f"La suma es {numero+10}")
    except:
        print("Ha ocurrido un error")
    else: #Ocurre si no se presenta ninguna excepcion
        print("Programa terminado correctamente")
        break
    finally:
        print("iteracion finalizada")


print("Programa terminado por completo")