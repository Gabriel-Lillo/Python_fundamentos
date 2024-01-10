

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5],
]

""" 
# Si queremos obtener solo los nombres de la lista de usuarios,
# podeamos ahecer la siquiente iteracion.
"""
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

"""Toda esa iteracion se puede hacer de otra manera en una sola linea."""
# Transformacion listado -> Es como .map()
#      elemento de la lista origen
#              |
nombres = [usuario[0] for usuario in usuarios]
print(nombres)


# Filtrar listado -> Es como .filter()
nombres = [usuario for usuario in usuarios if usuario[1] > 2] # En este ejemplo retornará solo los usuarios que tengan como ID un numero mayor que 2
print(nombres)                                                # solo retornará los mayores a 2

# Filtrar y transformar listado
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2] 
print(nombres)


""" METODOS .map() Y .filter() """
# Es otra alternativa en vez de utilizar las listas de comprencion 
# que están mas arriba

# .map()
nombres = list(map(lambda usuario: usuario[1] > 2, usuarios))
print(nombres)

# .filter()
menos_usuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios ))
print(menos_usuarios)


## Los metodos .map() y .filter() se utilizan mas en programacion funcional.