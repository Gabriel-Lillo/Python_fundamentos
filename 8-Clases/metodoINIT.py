'''
El metodo __init__ es mas recmendado utilizar
'''


class Usuario:

    def __init__(self, username, password): #-> Todas las reglas que vimos en Funciones aplican para los metodos ya que en esencia son funciones
        self.username = username
        self.password = password


user1 = Usuario("Gabrie", "1234")
user2 = Usuario("Andres", '5678')
user3 = Usuario("User3", '0987')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)