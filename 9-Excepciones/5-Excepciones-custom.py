""" Creando nuestras propias excepciones """

# ¿Por que hariamos nuestras propias Excepciones si podemos utilizar las que ya existen?
# La razon es porque podemos agregarles logica o agregar valores que podamos utilizar mas adelante.


class MiErrorPersonalizado(Exception): #-> Esta clase debe eredar de otra clase de error ya existente (puede ser cualquiera)
    "Esta clase es para representar mi error nuevo" #-> Este debe ser la documentacion que explica la razon de ser de este error.

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - Codigo de error: {self.codigo}"


def divicion(n=0):
    if n == 0:
        raise MiErrorPersonalizado("No se puede dividir por", 805) #-> Estos argumentos se asociaran a "mensaje" y "codigo" de la funcion __init__
    return 5 / n

try:
    divicion()
except MiErrorPersonalizado as e:
    print(e) 

