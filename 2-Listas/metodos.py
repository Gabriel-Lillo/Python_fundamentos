lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

# .sort  Ordenará la lista de menor a mayor
# .sort(reverse=True)  Ordenará la lista de mayor a menor

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)


# Para poder conocer el numero menor y mayor, podemos hacerlo de 2 formas:

lista.sort()
print(lista[0])
print(lista[-1])


# Funciones min() y max()

print(min(lista))
print(max(lista))

# Para saber si un elemento se encuentra en una lista se utiliza la palabra reservada "in"

print(10 in lista) # -> Entregará un valor booleano


# El metodo index() nos entregará el indice de un elemento

index = lista.index(5) #-> Este entregara el primer indice que encuentre en el caso que el valor exista mas de una vez
print(index)
