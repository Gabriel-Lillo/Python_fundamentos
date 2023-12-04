# Los diccionarioa son como las listas y tuplas con la salvedad que no se rigen con indices si no a una LLAVE!
# pueden ser modificados en el trascurso del programa

# * los diccionarios son equivalente a los JSON

# Existen dos formas para declarar un diccionario
diccionario = {}
diccionario = dict()


# { llave : el valor el cual queremos asociar}
diccionario = { "total": 55}
diccionario = {"total": 55, "descuento": True, "subtotal": 15}

diccionario = {"total": 55, 10: "Curso de Python", (1,2,3): True}
"""
Llaves:

Un strin ("total")
Un numero entero (10)
Una tupla que almacena numeros enteros (1,2,3)
"""

# Agregar nueva llave valor
diccionario['usuario'] = 'eduardo'

# Actualizar valor mediante una llave
diccionario['usuario'] = 'eduardo_gpg'

# Obtener valor mediante una llave
print(diccionario['usuario']) 


# Para obtener llaves y valores podemos utilizar los metodos .keys() .values()
diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel': 3, 'Gabriel': 4}

diccionario.keys()
diccionario.values()
for key, value in diccionario.items(): #-> .items() para recorres sus valores
    print(key, value)


# lOS DICCIONARIOS SON EQUIVALENTE A LOS JASON
usuario = {
    'nombre': 'Nombre del usuario',
    'edad': 28,
    'curso': 'Curso de python',
    'skills': {
        'programacion': True,
        'base_de_datos':False
    },
    'medallas': ['basico', 'intermedio']
}

