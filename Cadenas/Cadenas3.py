

cadena = "Hola mundo"
print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize()) #Hola mundo
print(cadena.title())      #Hola Mundo

cadena = "Hola mundo".count('hola'.capitalize())
print(cadena)   #2 veces se repite la o

cadena2 = "Hola mundo".find('a') #Tambien encuentra palabars
cadena3 = "Hola mundo mundo mundo".rfind('mundo') #Tambien encuentra palabars
print(cadena2)   #En que indice encuentra la rpiemra coincidencia de la o
print(cadena3)   

cadena4 = "1000".isdigit()
print(cadena4)

cadena5 = "ada".isalpha() #solo caracteres alfabeticos
print(cadena5)

cadena6 = "ada23?6".isalnum() #solo caracteres alfabeticos
print(cadena6)

cadena7 = "ada6".islower() #true si solo caracteres minusculas
cadena7 = "ada6".isupper() #true solo caracteres mayusculas
cadena7 = "ada6".istitle() #true solo si es un titulo
cadena7 = "    ".isspace() #true solo si todos son espacios
cadena7 = "hola mundo".startswith("h") #true solo si empieza con la letra o palabra que indicamos
cadena7 = "hola mundo".endswith("o")   #true solo si termina con la letra o palabra que indicamos
cadena7 = "hola mundo".split()   #te retorna una lista con una palabra por elemento ['hola', 'mundo']
cadena7 = "hola mundo".split('o')   #te retorna una lista con una palabra por elemento ['hola', 'mundo']
cadena7 = ",".join('javier ortega')   #te separa cada elemento de tu cadena con el caracter que elijas j,a,v,i,e,r, ,o,r,t,e,g,a
cadena7 = "         hola     ".strip()   #elimina en la cadena los espacios -> hola
cadena7 = "hola mundo".replace('o',' aqui iva una O ')   #reemplaza una letra o palabra con lo que indiques haqui iva una Ola mundaqui iva una O

print(cadena7)