# Para eliminar un elemento de una lista uilizaremos la palabra reservada "del"

diccionario = {'a': 1, 'b': 2,'c': 3,'d': 4}

# Primera forma para eliminar
del diccionario['a']
print(diccionario)


# Segunda forma de eliminar: metodo . pop()
diccionario.pop('b')
print(diccionario)

# Forma para vaciar el diccionario: .clear()
diccionario.clear()
print(diccionario)

