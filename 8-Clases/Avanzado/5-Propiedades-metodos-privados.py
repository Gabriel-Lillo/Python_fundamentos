""" Propiedade y metodos privados """
# Las propiedades privadas con propiedades (o variables) que no pueden ser modificadas y solo podemos acceder a ellas mediante la clase. se definen con __propiedad

class Perro:

    def __init__(self, nombre, edad): 
        self.__name = nombre 
        self.edad = edad

    def get_nombre(self):
        return self.__name #-> De esta forma podremos acceder directamente a una propiedad privada

    def set_nombre(self, nombre): #-> En el caso que quisieramos cambiar el valor de una propiedad privada
        self.__name = nombre
        return
    

    def habla(self): 
        print(f"{self.__name}Guau!")

    @classmethod
    def fabrica(cls):
        return cls("Chanchito feliz", 4) 
    
perro1 = Perro.fabrica()
perro1.habla()
print(perro1.__name) #-> Devolverá error porque al ser una propiedad privada no podemos acceder a ella directamente
print(perro1.get_nombre()) #-> De esta manera podemos acceder directamente a la propiedad mediante un metodo.


