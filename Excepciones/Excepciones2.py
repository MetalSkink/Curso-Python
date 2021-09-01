# Excepciones

def dividir():
    while True:
        try:
            num1 = float(input("Digite un numero: "))
            num2 = float(input("Digite otro numero: "))
            resultado = num1/num2
            print(f"El resultado es {resultado:.2f}")
        except ValueError:
            print("ERROR - debe de ingresar numeros")
        except ZeroDivisionError:
            print("ERROR - No se puede dividir un numero entre cero")
        else:
            break
        
dividir()