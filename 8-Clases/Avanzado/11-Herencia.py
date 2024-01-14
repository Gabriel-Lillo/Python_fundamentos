""" Herencias """

class Animal:
    def comer(self):
       print("comiento") 


class Perro(Animal): #-> Asignamos como parametro el nombre de la clase madre para heredar sus metodos.
    def pasear(self):
       print("paseando") 
    


class Chanchito(Perro): #-> Esta clase esta heredando de otra clase que ya tiene herencia. Esto se conoce como HERENCIA MULTINIVEL. No es recomendable usarlo mas de dos veces.
    def programar(self):
       print("programando")


pork = Chanchito()
pork.pasear()



