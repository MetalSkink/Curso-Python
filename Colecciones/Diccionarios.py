# Diccionarios

diccionario = {"azul":"blue","rojo":"red","verde":"green"}

diccionario["amarillo"] = "yellow" #Añadir un nuevo elemento
diccionario["azul"] = "BLUE" #Modificar un elemento ya existente
del(diccionario["rojo"]) #Borrar un elemento

print(diccionario)


diccionario2 = {"Xavier":{"edad":22,"estatura":1.73},"Salma":{"edad":20,"estatura":1.50}}
print(diccionario2)
print(diccionario2["Salma"])

# Diccionarios parte 2

equipo = {9:"Karim Benzema",
          7:"Eden Hazard",
          17:"Gareth Bale",
          11:"Marco Asensio",
          10:"Luka Modric"}

print(equipo.get(8,"No existe un jugador con ese Dorsal"))
print(10 in equipo)
print(equipo.keys())
print(equipo.values())
print(len(equipo))
equipo.clear()