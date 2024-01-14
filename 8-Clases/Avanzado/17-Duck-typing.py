""" Duck typing """
""" Si camina como pato y suena como pato, entonces es un pato!"""

# En este caso aun que no este declarado la clase Model() el codigo seguirá funcionando

class Usuario():
    def guardar(self):
        print("Guardando en BBDD")


class Sesion(): #-> Las Sesiones son las que permiten que un servidor identificar cuando un uasuario se está conectando y tambien saber a quien pertenece cada peticion. 
    def guardar(self):
        print("Guardando archivo")


def guardar(entidades): #-> entidad puede ser usuarios o sesiones
    for entidad in entidades:
        entidad.guardar()


usuario_cualquiera = Usuario()
sesion_cualquiera = Sesion()

guardar([usuario_cualquiera, sesion_cualquiera])



