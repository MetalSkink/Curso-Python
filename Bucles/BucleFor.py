# Bucle for

coleccion = [1,2,3,4] #Puede trabajar con listas,conjuntos, diccionarios 
coleccion2 = {"Xavier":22,"Salma":20,"Daniel":25}
coleccion3 = "Prestigitacion"

for i in coleccion3:
    print(f"{i}",end=" ")
print()
for clave,valor in coleccion2.items():
    print(f"{clave} -> {valor}")