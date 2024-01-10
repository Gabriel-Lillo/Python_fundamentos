""" Sets """
# Grupo , conjunto o coleccion de datos que no se puede repetir y tampoco está ordenada

primer_set = {1, 1, 2, 2, 3, 4}
print(primer_set)

# Puede utilizar los mismos metodos que las listas
#primer_set.add(5)
#primer_set.remove(1)


# podemos transformar cualquier iterable a un set .set()
segundo_set = [3, 4, 5] #-> cuando se utiliza [] sabemos que no es un set sino una lista
segundo_set = set(segundo_set)


""" OPERADORES """
# | = de unión
print(primer_set | segundo_set) #-> Unifica dos sets

# & = de intersección
print(primer_set & segundo_set) #-> Devuelve solo los elementos que existe en ambos sets

# - = de diferencia
print(primer_set - segundo_set) #-> Devuelve solamente los datos que se encuentranen el conjunto de la izq. en relacion a los que existens en el segundo set

#  = de diferencia simetrica
print(primer_set ^ segundo_set) #-> Devuelve los elementos que existen en ambos pero no los elementos que se repiten entre ellos.


## ESTAS OPERACIONES SE UTILIZAN MUCHISIMO CUANDO SE MANEJAN DATOS REALES

""" PROBLEMAS """
# No están ordenadas
# No podemos acceder a sus datos

if 5 in segundo_set:
    print("Hola mundo")