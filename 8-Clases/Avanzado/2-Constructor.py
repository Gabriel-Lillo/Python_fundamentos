""" Constructor """
# El Constructor se define utilizando la palabra reservada __init__ 
# Siempre tendrá como primer atributo self , que hace referencia a la instancia.

class Perro:
    def __init__(self, nombre, edad): # Podemos darle valores como parametros para despues definirlos.
        self.name = nombre #-> De esta manera se definen los valores entregados como parametros. Se denominan PROPIEDADES!
        self.edad = edad

    def habla(self):
        print(f"{self.name} dice: Guau!") #-> Podemos acceder a las propiedades self. facilmente


mi_perro = Perro("Chanchito", 2)
mi_perro2 = Perro("Gabriel", 5)
mi_perro.habla()
# print(mi_perro.name)


