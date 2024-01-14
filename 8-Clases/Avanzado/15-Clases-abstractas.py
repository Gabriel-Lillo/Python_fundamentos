""" Clases abstractas """
# Nos referimos a clases abstractas a las clases que no generan instancias,
# pero sin embargo podemos heredar sus propiedades y metodos.

# importamos abstractclass
from abc import ABC, abstractmethod



class Model(ABC): #-> Hereda todo lo de la clase abc para que sea Abstracta
    @property #->  Usamos el decorador para definir tabla como propiedad
    @abstractmethod #-> Usamos este decorador que importamos de abc para definir que la propiedad es abstracta
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self): #-> Lo definimos como abtracto para despues implementar el metodo en la clase usuario.
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):  
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("Guardando usuario")
    


usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(123)
