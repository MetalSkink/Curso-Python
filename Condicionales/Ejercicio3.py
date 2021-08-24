'''
Hacer un programa que pida un caracter e indique si es una vocal
o no
'''

char = input("Dame un caracter -> ").lower()

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("Es una vocal")
else:    
    print("No es una vocal :(")