#Ejercicio 4

'''
Hacer un programa para ingresar el radio de un circulo y se 
reporte su area y la longitud de la circunferencia

'''
import math

radio = float(input("Ingrese el radio -> "))

area = math.pi * (radio**2)
long = 2*math.pi*radio
print(f"area: {area:.2f} longitud: {long:.2f}")