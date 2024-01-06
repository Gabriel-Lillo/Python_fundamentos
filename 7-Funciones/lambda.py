'''
Las funciones en python son "Ciudadanos de primera clase", es decir, las funciones
pueden ser asignadad a variables, como argumentos de otras funciones,
o funciones pueden retornar otras funciones
'''

def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32


mi_funcion = centigrados_a_farhenheit

print(type(mi_funcion)) #-> tipo funcion
print(mi_funcion(10))


# Una funcion lambda o tambien conocida como FUNCION ANONIMA, es una funcion expresada en una sola linea de codigo ademas de no poseer un nombre
# ya que este tipo de funciones realizan tareas muy pequeñas
'''
Estructura:
lambda <parametro> : <cuerpo de la funcion>
'''
funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(10))

'''
Otros ejemplos:
'''
sin_parametros = lambda : True
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3
con_asterisco = lambda *args, **kwargs : len(args) + len(kwargs)
