'''
HERENCIA
'''
class Mascosta: # -> Clase padre
    def comer(self):
        print('La mascota come.')

    def dormir(self):
        print('La mascota duerme.')


class Perro(Mascosta): #-> Clase hija
    pass

class Gato(Mascosta): #-> La clase padre puede heredar N cantidad de veces. Basta con colocar como parametro el nombre la la clase padre
    pass

duke = Perro()

duke.comer()
duke.dormir()

michi = Gato()

michi.comer()
michi.dormir()

'''
HERENCIAS MULTIPLES

En python, a diferencia de otros lenguajes, una clase puede heredar de multiples clases
'''
class Animal(): #-> Clase padre
    def comer(self):
        print('El animal come.')

    def dormir(self):
        print('El animal duerme.')
    

class Mascosta(Animal): # -> Clase padre e hijo
    pass

class Felino():
    def cazar(self):
        print('El felino caza')

        
class Gato(Mascosta,Felino): #-> La clase mascota al heredar los metodos de Animal, la clase Gato puede hacer uso de ellos.
    pass


patricio = Gato()

patricio.comer()
patricio.dormir()
patricio.cazar()


# ** Mientras mayor sesa el nivel gerarquico, la clase será mas abstracta

