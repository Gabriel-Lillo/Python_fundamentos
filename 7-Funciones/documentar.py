# Docstring = Es un comentario que se coloca en la primera linea de codigo de una funcion (Por convencion se utiliza "tres comillas dobles")
# __doc__ (Modulos, Clases, Metodos y funciones)
# help() (Modulos, Clases, Metodos y funciones)

def suma(numero_1, numero_2):
    """
    La funcion suma 2 números entreros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.

    TODO:
        *
    """
    return numero_1 + numero_2

print(suma.__doc__) # -> en el atributo __doc__ estará almacenado todo el Docstring
print(help(suma))