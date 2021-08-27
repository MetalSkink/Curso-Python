# Instrucción continue y break

for i in range(10):
    if i == 5:
        continue #No ejecuta el resto del ciclo y pasa a la siguiente iteracion
    if i == 7:
        break    #Rompe el ciclo 
    print(i)

print("PROGRAMA FINALIZADO")