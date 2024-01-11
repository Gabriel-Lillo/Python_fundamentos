'''
Podemos dividir los atributos en dos tipos

Attrs de clase : Atributos que le pertenecen a una clase. Para poder usarlos tenemos que usar dicha clase
Attrs de instancia : Atributos que le pertenecen a un objeto. Para usarlos trabajaremos con un objeto 
'''

class Usuario:
    #Attrs de Clase = basta con definir variables dentro de la clase
    username = ''
    email = ''

#para modificar los atributos
Usuario.username = 'User1'
Usuario.email = 'email.ejemplo@gmail.com'

#para usar los atrubutos de clase usamos en conjunto la clase
print(Usuario.username)
print(Usuario.email)


#Attrs de instancia
class Usuario2:
    username = 'username por default'
    email = ''

user1 = Usuario2() # -> Se crea un objeto
'''
De manera interna, Python utiliza un metatributo ( __dict__ ) así poder identificar los atributos de una clase para poder compartirlos a un objeto
__dict__
1.- Verifica si el attrs existe dentro del objeto
2.- Verifica si el attrs existe dentro de la clase -> solo lectura
3.- Lasza un error en el caso que ninguno de los anteriores ocurra
'''
print(user1.__dict__) # Diccionario
print(user1.username)

print(id(user1.username))
print(id(Usuario.username)) #-> comparten el mismo id ya que son el mismo atributo


'''
Atributos dinamicos a los objetos

* A la larga no es muy buena idea agregar atributos de manera dinamica, porque pueden generar problemas. 
  lo comun es estandarizar los atributos en una clase y crear objetos segun su clase.
'''
user1.username = 'Gabriel' #-> añadimo un attrs al objeto
user1.password = '1234' # -> si un atributo no existe en el objeto lo creará

print(id(user1.username)) # -> Attrs de instancia correspondiente al objeto
print(id(Usuario.username)) #-> Ahora son distintos id

print(user1.__dict__) # Diccionario




