# Como añadir u obtener elementos de una diccionario
# La llave de un diccionario siempre debe ser un string
punto = {"x" : True}

elementos = {}

# Añadir
elementos['nombre'] = 'Gabriel' # -> si la llave no existe lo crea
elementos[(1,2,3)] = 'La llave en una tupla'
print(elementos)



# Modificar
elementos['nombre'] = 'Andres' # -> Si la llave ya existe modifica el valor
print(elementos)


# Obtener
diccionario = {'a': 1, 'b': 2,'c': 3,'d': 4}
valor = diccionario['d']
print(valor)
# Obtener con metodo .get()
valor = diccionario.get('z', 'este atributo puede ser cualquier valor que asignemos') # -> .get() puede recibir un segundo atributo que entregará en caso de no encontrar la llave (ej. Booleanos)
print(valor)

# Otra forma de añadir metodo .setdefault()
valor = diccionario.setdefault('e', 5)
print(diccionario)

