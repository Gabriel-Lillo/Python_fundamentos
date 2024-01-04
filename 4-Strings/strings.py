# Strings y listados

lenguajes = 'Python Ruby Java Rust C++ C'

# El metodo split() retornará una listado a partir del string. Como argumento recive el separador de elementos 
#por defecto separa los elementos por espacios. ej. se puede separar por - split('-')

listado_lenguajes = lenguajes.split()

print(listado_lenguajes)


# El metodo join() retornará un string a partir de una lista
 
lenguajes = ['Python', 'Ruby', 'Java', "Rust"]

string_lenguajes = ' '. join(lenguajes)

print(string_lenguajes)


# El netodo len() nos permite identificar la cantidad de caracteres que contiene un string

nombre_curso = "Ultimate Python"

print(len(nombre_curso)) # -> retornará 15 inclutyendo los espacios

# Para obtener valores según su indice en un string
print(nombre_curso[0])
print(nombre_curso[0:8])
print(nombre_curso[:8]) # hasta el numero indicado a la derechas de los dos puntos
print(nombre_curso[9:]) # desde el numero indicado hasta el final