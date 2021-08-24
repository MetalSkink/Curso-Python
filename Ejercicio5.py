#Ejercicio 5
'''
Una tienda ofrece un descuento del 15% sobre el total de la compra
y un cliente desea saber cuanto debera pagar finalmente su compra
'''

total = float(input("Total -> "))

# descuento = total * 0.85
total *= 0.85

print(f"El precio final fue ${total:.2f}")