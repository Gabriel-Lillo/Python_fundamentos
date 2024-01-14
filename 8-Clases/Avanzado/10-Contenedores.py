""" Contenedores """
# Esto se refiere a como meter objetos dentro de otros objetos

# Intentaremos introducir un Producto a una Categoria
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):#-> Utilizamos __str__ para imprimir en pantalla la informacion que nos interesa.
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
        
    def agregar(self, producto): #-> Este metodo se encargará de ir ingresando los productos a la lista de productos.
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 500)
deportes = Categoria("Deportes", [kayak,bicicleta])#-> Podemos entregar directamente una lista como parametro, sin necesidad de almacenarlo en una variable.

deportes.agregar(surfboard)
deportes.imprimir() #-> Devolverá todos los productos agregados