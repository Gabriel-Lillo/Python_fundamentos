""" Anulacion de metodos o Method Override"""

#  La anulación de metodos es cuando tomamos un metodo que hayamos heredado y reemplazarlo por otro para cambiar su funsionalidad.

class Ave:
    def vuela(self):
        print("vuala ave")

class Pato(Ave):
    def vuela(self): #-> Aqui estamos reemplazando el metodo "vuela" de la clase Ave
        print("vuela pato")
        super().vuela()#-> Con super() podemos acceder al metodo original de la clase Ave.

pato = Pato()
pato.vuela()


""" Otra forma de hacerlo es con el contructor """

# class Ave:
#     def __init__(self): # Aquí setteamos el metodo 
#         self.volador = "volando"

#     def vuela(self):
#         print("vuala ave")

# class Pato(Ave):
#     def __init__(self):
#         super().__init__() # Aquí llamamos el metodo de la clase padre
#         self.nada = "nadando"

#     def vuela(self):
#         print("vuela pato")
#         super().vuela()

# pato = Pato()
# pato.vuela()
# print(pato.volador, pato.nada )