# Con el ciclo for podemos iterar por cada elementos de una coleccion de datos ( String, listas, tuplas, diccionarios)
# Principalmente se utiliza para iterar una lista de elementos

usuarios = [ 'usuario1','usuario2', 'usuario3', 'usuario4',] #-> las tuplas, listas siempre se declaran en plural

for usuario in usuarios:
    print(usuario)


for numero in range(5):
    print(numero, numero * " hola mundo")

# Ejemplo para encontrar un valor
"""For else"""

buscar = 10    
     
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break #-> Es importante interrumpir el ciclo cuando se haya encontrado el elemento.
else:
    print("No encontré el numero :(")


