'''
Colecciones - Ejercicio 1:
Escriba un programa donde tenga una lista y que, a continuación, elimine los elementos repetidos, por último mostrar la lista.
'''

lista = [1,2,3,4,4,3,5,1,"molino","viento","molino"]

conjunto = set(lista)

lista = list(conjunto)

# lista = list(set(lista))    SOLUCION ALTERNA

print(lista)

