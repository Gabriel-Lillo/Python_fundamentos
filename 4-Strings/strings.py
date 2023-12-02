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
