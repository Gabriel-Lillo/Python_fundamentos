""" Metodos magico """

# Los metodos magicos son metodos que se van a ejecutar cuando no lo estemos llamando directamente.
# TOOODOOS lo metodos magicos empieza y terminan con __ (__metodomagico__)


class Perro:
    def __init__(self, nombre, edad): #-> El constructor __init__ es una metodo magico ya que este se ejecuta automaticamente cuando hacemos una instancia.
        self.nombre = nombre
        self.edad = edad

    def __str__(self): #-> metodo magico que nos premite determinar que es lo que queremos que muestre en la terminal al momento de imprimir la clase en pantalla.
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("chanchito", 7)
print(perro)
texto = str(perro) #-> Tambien podemos imprimir informacion de la clase transformandolo en string.
print(texto)



"""
Podemos ver todo el listado de metodos magicos que tenemos disponibles para nuestra clase.
estos metodos magicos están disponibles por herencia

perro.__  (aparecerá un listado para autocompletar)


Tambien podemos revizar la documentacion buscando: "magic methods python"
link de //rszalski.github.io
"""


