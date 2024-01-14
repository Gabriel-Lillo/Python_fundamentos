""" Extender tipos nativo """

#Esto se refiere a crear metodos basados en los tipos nativos.

# Por ejemplo tipo list()

lista = list([1, 2, 3])
lista.append(4)
lista.insert(0,21)

print(lista)

# Lo podemos hacer de esta otra manera.
class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista2 = Lista([1, 2, 3])
lista2.append(4)
lista2.prepend(22) #-> Creamo un metodo como extension de las funciones de list() para que funciones como .append() dando solo un parametro en vez de dos como en .insert().
print(lista2)

