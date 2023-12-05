'''
Estructura del test dentro del Docstring:

# >>> nombre_funcion(argumento_1, argument_n)
  valor esperado

  
para ejecutarlo se llama en consola con:

    python -m archivoAtestear.py
'''

# __doc__ (Modulos, Clases, Metodos y funciones)
# help() (Modulos, Clases, Metodos y funciones)

def suma(numero_1, numero_2):
    """
    La funcion suma 2 números entreros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.

    >>> suma(10, 20)
    30
    
    >>> suma(100, 200)
    300
    """
    return numero_1 + numero_2
