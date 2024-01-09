""" Filas """

from collections import deque

# Las filas tienen la caracteristica de ser FIFO = first in, first out(Primero en llegar , primero en irse)

lista = [1, 2, 3, 4]

# deque() es una CLASE que recive como argumento una lista
fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)

# Para eliminar elemento se usa .popleft()
fila.popleft()

if not fila: #-> da como resultado un Falsy
    print("fila vacía")