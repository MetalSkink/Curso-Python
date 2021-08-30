# Argumentos por valor o por referencia

def doblarValor(numero):
    numero *=2
    print(numero)

def doblarValores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
n = 5
doblarValor(n) # Argumentos por valor
print(n)

m = [5,10,15,20] 
doblarValores(m) #Argumentos por referencia, las colecciones se pasan por referencia por defecto
print(m)

m = [5,10,15,20]
doblarValores(m[:]) # Argumentos por valor
print(m)

