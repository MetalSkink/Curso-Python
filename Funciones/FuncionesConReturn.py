# Funciones con retorno de valor

def multiplicar(num1,num2):
    mult = num1*num2
    return mult

result = multiplicar(3,4)
print(result)

def prueba():
    return "hola",45,[1,2,3]

c,n,l = prueba()

print(c)
print(n)
print(l)