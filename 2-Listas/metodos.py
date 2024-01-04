lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

# .sort  Ordenará la lista de menor a mayor
lista.sort()
print(lista)

# .sort(reverse=True)  Ordenará la lista de mayor a menor
lista.sort(reverse=True)
print(lista)


# Para poder conocer el numero menor y mayor, podemos hacerlo de 2 formas:
lista.sort()
print(lista[0])
print(lista[-1])

# sorted() Es como sort() con la única diferencia que devuelve una NUEVA lista 
lista2 = sorted(lista)

# Funciones min() y max()
print(min(lista))
print(max(lista))


# Para saber si un elemento se encuentra en una lista se utiliza la palabra reservada "in"

print(10 in lista) # -> Entregará un valor booleano


# El metodo index() nos entregará el indice de un elemento

index = lista.index(5) #-> Este entregara el primer indice que encuentre en el caso que el valor exista mas de una vez
print(index)
