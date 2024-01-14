""" Polimorfismo """

from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass



class Usuario(Model):
    def guardar(self):
        print("Guardando en BBDD")


class Sesion(Model): #-> Las Sesiones son las que permiten que un servidor identificar cuando un uasuario se está conectando y tambien saber a quien pertenece cada peticion. 
    def guardar(self):
        print("Guardando archivo")


def guardar(entidades): #-> entidad puede ser usuarios o sesiones
    for entidad in entidades:
        entidad.guardar()


usuario_cualquiera = Usuario()
sesion_cualquiera = Sesion()

guardar([usuario_cualquiera, sesion_cualquiera])


# Si nos fijamos tenemos el metodo guardad en dos clases distintas y a su vez
# pueden ser ejecutados en la funcion guardar. A esto se le llama polimorfismo
# En pocas palabras son metodos que cumples con una interfas para que puedan ser ejecutadas 
