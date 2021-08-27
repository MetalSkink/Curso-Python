'''
Bucles - Ejercicio 11:
Hacer un programa que simule una agenda de contactos. 
Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono, 
el programa tendrá el siguiente menú de opciones:

1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4. Salir
'''

agenda = {"Xavier":2721362362,"Salma":2723666989,"Ruben":2721369988,"Josue":2723659966}

while True:
    print("\n\t.:MENU:.",
          "¿Que operacion quiere realizar",
          "1. Nuevo contacto",
          "2. Borrar contacto",
          "3. Ver contactos existentes",
          "4. Salir",sep="\n")
    operacion = int(input("-> "))

    if operacion == 1:
        nombre = input("Ingrese el nombre de contacto: ")
        numero = int(input("Ingrese el numero: "))
        if nombre not in agenda:
            agenda[nombre] = numero
            print("Contacto agregado con exito!!")
        else:
            print("Este nombre de contacto ya existe")
    elif operacion == 2:
        for i in agenda:
            print(f"{i}")
        delSelector = input("Que contacto quiere borrar? -> ")
        if nombre in agenda:
            del(agenda[delSelector])
            print("Contacto eliminado!!")
        else:
            print("Ese contacto no existe")
    elif operacion == 3:
        print("\tCONTACTOS")
        for i in agenda:
            print(f"{i} - {agenda[i]}")
    elif operacion == 4:
        print("Hasta luego que pase buena tarde :D")
        break