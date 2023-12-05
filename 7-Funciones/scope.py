# Comportamiento de las variable dentro y fuera de las funciones


animal = 'Leon' # -> Variable global (pueden ser utilizadas en cualquier bloque de codigo; Funciones, condiciones o ciclos)
print(animal)

def imprimir_animal():
    global animal #-> Siqueremos modificar una variable global dentro de un bloque de codigo, utilizamos la palabre reservada "global"
    animal = 'Ballena'

    #animal = 'Ballena' # -> Variable local (no existen fuera de este bloque de codigo)
    tipo = 'Mamifero' #-> Variable local
    print(animal)
    print(id(animal))
    print(tipo)

imprimir_animal()

print(animal) # -> Muestra "animal" que fue declarado globalmente o el valor que fue modificado dentro de un bloque de codigo
print(id(animal))

#print(tipo) # -> dará error porque llama a una variable que no existe globalmente