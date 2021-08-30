# Funciones - Ejercicio 3:

# Crear un programa que tenga una lista de clientes, cada cliente tiene su Nombre, 
# Apellido y DNI. El programa tendrá el siguiente menú de opciones:

# 1. Agregar nuevo cliente
# 2. Mostrar todos los clientes
# 3. Mostrar cliente por DNI
# 4. Eliminar cliente
# 5. Salir
# PD: Cada opción de menú se realizará con una función
clientes = []

def agregar_cliente(nombre, apellido, dni):
    cliente = {}
    cliente['nombre'] = nombre
    cliente['apellido'] = apellido
    cliente['dni'] = dni 
    clientes.append(cliente)

def mostar_clientes():
    if len(clientes) > 0:
        for i in clientes:
            print(f"Nombre {i['nombre']}, Apellido: {i['apellido']}, DNI: {i['dni']}")
    elif len(clientes) == 0:
        print("No hay clientes registrados")

def mostar_cliente(dni):
    for i in clientes:
        if i['dni'] == dni:
            print(f"Nombre {i['nombre']}, Apellido: {i['apellido']}, DNI: {i['dni']}")
            return True
    return False

def eliminar_cliente(dni):
    for i in clientes:
        if i['dni'] == dni:
            clientes.remove(i)
            return True
    return False

while True:
    print("\n\t.:MENU:.",
          "1. Agregar nuevo cliente",
          "2. Mostrar todos los clientes",
          "3. Mostrar cliente por DNI",
          "4. Eliminar cliente",
          "5. Salir",sep="\n")
    operacion = int(input("-> "))
    print()
    if operacion == 1:
        nombre = input("Nombre del cliente -> ")
        apellido = input("Apellido del cliente -> ")
        dni = input("dni del cliente -> ")
        agregar_cliente(nombre,apellido,dni)
    elif operacion == 2:
        mostar_clientes()
    elif operacion == 3:
        dni = input("dni del cliente -> ")
        if mostar_cliente(dni):
            print("Cliente encontrado")
        else: 
            print("Cliente no encontrado")
    elif operacion == 4:
        dni = input("dni del cliente -> ")
        if eliminar_cliente(dni):
            print("Cliente eliminado")
        else: 
            print("Cliente no existe")
    elif operacion == 5:
        break
    else:
        print("Operacion no admitida")

