# Conjuntos

conjunto = set()

conjunto = {1,2,3,4,5, "Hola", 4.56}

conjunto.add(89)
conjunto.discard(3)
print(3 in conjunto)
print(3 not in conjunto)

print(conjunto)

conjunto.clear()
print(conjunto)

a = {1,2,3}
b = {3,4,5}
z = frozenset({1,2,3,4,5}) #Hacer un conjunto inmutable para que no se pueda modificar

print(a==b)
print(len(a))

c = a | b #Unir conjuntos
d = a & b #Interseccion conjuntos
e = a - b #Diferencia, elementos de A que no estan en B
f = a ^ b #Diferencia simetrica, elementos que estan en a o b pero no en ambos, lo contrario a la interseccion

print(a.issubset(c))    #Saber si A es un subconjunto de C
print(c.issuperset(a))  #Saber si C es un superconjunto de A
print(a.isdisjoint(b))  #Saber si A no comparte ningun elemento de B

print(c)
print(d)
print(e)
print(f)