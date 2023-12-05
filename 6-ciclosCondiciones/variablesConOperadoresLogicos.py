# Asignar valores mediante operadores logicos


variable = 'Cody' or 'CodigoFacilito'
print(variable) #-> retornará 'Cody'

variable = '' or 0 or [] or True
print(variable) #-> retornará True 


# Ejemplo practico 

listado = [] # -> listado vacío da resultado False
nombre = 'Cody'

"""
if listado: 
    variable = listado
else:
    variable = nombre
"""

variable = listado or nombre #-> en este ejemplo asignará el valor que sea True

print(variable)