""" Descontructor """

# El descontructor es un metodo magico como __init__  pero hace lo opuesto. elimina una clase de la memoria
# se define con: __del__

class Perro:
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        return print(f"Chao perro {self.nombre}")

    def __str__(self): 
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("chanchito", 7)
del perro