""" Ejemplo real con herencias """

"""
Al manejar bases de datos podemos:

- Leer
- Crear
- Actualizar
- Eliminar

crearemos una Clase que pueda realizar todas esas acciones.
"""

class Model(): 
    tabla = False
    nombre = ""
    _id = 0
    _id_usuario = 0
    def __init__(self):
        if not self.tabla: #-> Validamos si existe la tabla
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id): #-> Anteponemos un _ en id porque ya existe una palabra reservada con id en python. 
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


    def eliminar_tabla(self):
        print(f"La tabla {self.tabla} con id : {self._id} ha sido eliminado")

    def eliminar_usuario(self):
        print(f"El usuario {self.nombre} con id : {self._id_usuario} ha sido eliminado")



class Usuario(Model):
    tabla = "Usuario"
    


usuario = Usuario() #-> Creamos una instancia de la clase Usuario()

usuario.guardar()
Usuario.buscar_por_id(123) #-> Buscamos el id desde la clase Usuario() con @classmethod
usuario.eliminar_usuario()


class Pais(Model):
    tabla = "Pais"
    _id = 8760

chile = Pais()
chile.guardar()
chile.eliminar_tabla()
