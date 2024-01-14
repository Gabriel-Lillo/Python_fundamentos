""" Tipos de excepciones """

# Python nos prmite controlar los errores y tambien identificar el tipo de error.
# Podemos ejecutar distinta logica segun el error

# Tipo Exception:  Maneja absolutamente todas las excepciones
# Tipo VulueError: Maneja un posible error de un valor ungresado.
# Tipo NameError: Maneja posibles errores de nombres
""" 
Existen muchas excepsiones mas. podemos revisar en la documentacion.
Buscar en el explorador: python errors and exceptions
 "Built-in Exceptions"
"""

try:
    n1 = int(input("Ingresa primer número"))
# except Exception as e: #-> Como convencion se asigna como "e" o "ex"
#     print(type(e))
except ValueError as e:
    print("Ha ocurrido una error")
except NameError as e:
    print("Ha ocurrido una error")