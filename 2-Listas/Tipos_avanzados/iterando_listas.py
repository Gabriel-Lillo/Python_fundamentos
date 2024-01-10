


mascotas = ["Rocky", "Pelusa", "Pulga", "Copito"]

# Podemos usar el mismo metodo de desempaquetado en las tuplas
for indice, mascota in enumerate(mascotas): #-> enumerate() es una funcion que entrega un listado de tuplas con el indice del elemento
    print(mascota)
    print(indice, mascota)
