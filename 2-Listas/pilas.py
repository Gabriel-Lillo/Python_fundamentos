""" Pilas """

# Las pilas tienen la propiedad LIFO = Last in First out( ultimo en llegar, primero en salir)

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

ultimo_elemento = pila.pop()
print(ultimo_elemento)

print(pila[-1])

if not pila:
    print("pila vacía")