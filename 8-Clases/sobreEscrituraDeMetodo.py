'''
Sobreescritura de Metodo

Tambien conocida como sobrecarga de metodos, es una de los temas principales al momento de trabajar con programacion 
orientado a objetos.

Consiste en que una clase hija puede modificar el comportamiento de los metodos de la clase padre,
para que estos se adecuen a la clase hija
'''

class Animal(): #-> Clase padre
    def comer(self):
        print('El animal come.')

    def dormir(self):
        print('El animal duerme.')
    

class Mascosta(Animal): # -> Clase padre e hija
    def comer(self): #-> Para modificar un metodo de la clase padre, basta con redefinir el metodo en la clase hija
        super().comer() #-> Nos permite acceder de manera inmediata al metodo de la clase padre
        print('La mascota come.') 


class Felino():
    def cazar(self):
        print('El felino caza.')

        
class Gato(Mascosta,Felino): #-> Clase Hija
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self): #-> Para modificar un metodo de la clase padre, basta con redefinir el metodo en la clase hija
        print(f'{self.nombre} come.')

    def dormir(self):
        print(f'{self.nombre} duerme.')


patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()

'''
Funcion super() = Nos permite acceder de manera inmediata al metodo de la clase padre
'''





