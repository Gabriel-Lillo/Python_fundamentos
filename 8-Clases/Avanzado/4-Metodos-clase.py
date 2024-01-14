""" Metodos de clase """
# Los Metodos funcionan similar a los atributos


class Perro:
    patas = 4 

    def __init__(self, nombre, edad): 
        self.name = nombre 
        self.edad = edad

    @classmethod #-> classmethod se utiliza para indicar que el metodo le pertenece a una clase
    def habla(cls): #-> cls Es una convencion que se utiliza para cuando estamos creando metodos de clases para referirnos a la clase misma
        print("Guau!")

    @classmethod
    def fabrica(cls):
        return cls("Chanchito feliz", 4) #-> cls es la referencia de la clase. Podriamos perfectamente cambiar cls por Perro (que es el nombre de la clase)

Perro.habla()

# Si quisieramos crear una instancia N cantidad de veces...
perro1 = Perro("Chanchito", 2)
perro2 = Perro("Boby", 3)
# En vez de crear un instancia uno a uno, podemos llamar el metodo "fabrica" de la clase
perro3 = Perro.fabrica()
print(perro3.edad, perro3.name)
