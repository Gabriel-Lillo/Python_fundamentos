""" Herencias Multiples """

class Animal:
    def comer(self):
       print("comiento") 

    def pasear(self):
       print("paseando animales") 

class Perro: 
    def pasear(self):
       print("paseando al perro") 
    

# En el caso que queramos heredar metodos de dos clases distintas, indicamos los nombres como parametros.
class Chanchito(Perro, Animal): 
    def programar(self):
       print("programando")


pork = Chanchito()
pork.pasear()

"""
En la vida real es probable que dos clases tengan el mismo metodo pero con una ligera diferencia.
Esto puede genrar un problema al momento de heredar ciertos metodos.


Existe una regla para evitar ese problema:
- Eliminamos el metodo que está duplicado en otra clase
- Generar clases pequeñas solamente para heredar
"""
# ESTA ES LA FORMA CORRECTA PARA UTILIZAR LA HERENCIA MULTIPLE
class Caminador:
    def caminar(self):
       print("caminando") 

class Volador: 
    def volar(self):
       print("volando") 
    
class Nadador(Perro, Animal): 
    def nadar(self):
       print("nadando")

class Pato(Volador, Nadador, Caminador): 
    def programar(self):
       print("programando")


pork = Chanchito()
pork.pasear()






