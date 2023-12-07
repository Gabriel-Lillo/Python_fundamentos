'''
Metodos

* Al igual como existen 2 metodos de atributos (Attrs de clase; attrs de instancia). podemos separar en 
  dos tipos los metodos

  Metodo de instancia = Le pertenecen al objeto (self: como primer parametro)
  Metodo de clase = Le pertenece a la clase (cls: como primer parametro)

* A la larga NO es muy buena idea agregar atributos de manera dinamica, porque pueden generar problemas. 
  lo comun es estandarizar los atributos en una clase y crear objetos segun su clase, para que así no existan 
  objetos con mas o menos atributos.
'''

# Para crear un metodo es necesario crear un funcion dentro de la clase
class Usuario:

    def inicializar(self, username, password): #-> Para que esta funcion sea un metodo, obligatoriamente debe tener, al menos, un parametro, por convencion, "self"
        # Añadimos attrs al objeto
        self.username = username
        self.password = password


user1 = Usuario()
user2 = Usuario()

print(user1.__dict__)
print(user2.__dict__)

user1.inicializar('Gabriel', '1234') #-> Al llamar el metodo (funcion) de la clase el objeto obtendrá los atributos
user2.inicializar('Andres', '5678') #-> Podemos agregar como argumento los datos que queremos agregarles a los atributos

print(user1.__dict__)
print(user2.__dict__)


