""" Decorador Property """

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property #-> este es un decorador parecido a @classmethod. Este no permite trasformar un metodo a una propiedad.
    def nombre(self): #-> Recive el nombre de una propiedad cualquiera
        print("pasando por getter")
        return self.__nombre
     
    @nombre.setter #-> al definir un metodo con el decorador @property, este mismo puede ser utilizado como decorador
    def nombre(self, nombre): #-> Este metodo nos permite controlar de que la clase perro reciva un nombre valido y no un string vacío.
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return  


perro = Perro("Choclo")
print(perro.nombre)

