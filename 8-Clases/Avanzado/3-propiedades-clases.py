""" Propiedades de clase """


class Perro:
    patas = 4 #-> Podemos asignar variables de clase que serán asociadas a todas las instancias.

    def __init__(self, nombre, edad): 
        self.name = nombre 
        self.edad = edad

    def habla(self):
        print(f"{self.name} dice: Guau!")


Perro.patas = 3 #-> Podemos modificar la propiedad de la clases cuando queramos 
mi_perro = Perro("Chanchito", 2)
mi_perro.patas = 5 #-> O tambien podemos modificar la propiedad de la clase a una sola instancia en especifico.
mi_perro2 = Perro("Andres", 5)
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
