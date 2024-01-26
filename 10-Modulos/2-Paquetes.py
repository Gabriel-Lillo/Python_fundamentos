""" Paquetes """
# Los paquetes, a diferencia de los modulos, apuntan a carpetas.
# Para crear una carpeta para usarlo como paquete debemos crear un archivo con nombre __init__.py en la carpeta.

from usuarios.acciones import guardar
            # acciones se refiere a un modulo que se encuantra en la carpeta

# En el caso que queramos importar todos los modulos de un paquete:
# from usuario import acciones

guardar()