""" Invocar excepcion """

""" 
Existen muchas excepsiones mas. podemos revisar en la documentacion.
Buscar en el explorador: python errors and exceptions
 "Built-in Exceptions"
"""


def divicion(n=0): #-> El cero es indivisible con cualquir numero. No se puede!
    if n == 0:
        raise ZeroDivisionError(f"No se puede dividir por {n}") #-> Todos los argumentos que le pasemos a la clase ZeroDivisionError se pasan automaticamente a Eexcept as e
    return 5 / n

try:
    divicion()
except ZeroDivisionError as e:
    print(e) #-> Al imprimir "e" podemos ver los argumentos asignados al error. Asi es como invocamos la exepcion.

"""
NOTA:
1.- No debemos lanzar excepciones muy seguido porque son muy costosas en rendimiento
    pero ser explicitos en los errores de vez en cuando no es tan terrible
2.- Tambien podemos crear nuestras propias excepciones
"""