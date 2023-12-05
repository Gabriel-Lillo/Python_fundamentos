# Los closures están estrechamente relacionadas con las funciones anidadas y alcances de las variables 

def funcion_principal():
    a = 'a' # -> Variables locales con alcance a todo el codigo ue esté destro de esta funcion
    b = 'b'

    def funcion_anidada():
        c = 'c' # -> Variable local

        nonlocal b # -> esta palabra reservada nos sirve para indicar que no queremos modificar la variable "b" en esta nueva funcion
        b = 'Cambio de valor'

        print(a)
        print(b)

    funcion_anidada()
    #print(c) -> Dará error porque es una veriable declarada localmente en la "funcion_anidada"

funcion_principal()


# Retornar funciones
def saludar():

    def mostra_mensaje():
        print('Hola, no encontramos en el curso de python.')
    
    return mostra_mensaje

respuesta = saludar()

#print(respuesta)
respuesta() #-> Así llamamos a una funcion mediante una variable


# ****************CLOSURES********************
# Los Closure son funciones que pueden generar de forma dinamica a otra funcion, y esta nueva funcion 
# puede acceder a la variables locales aún cuando la primera haya finalizado.

def saludar(username):
    mensaje = f'Hola {username}' # -> Variable local

    def mostrar_mensaje():
        print(mensaje)
    
    return mostrar_mensaje

username = 'Gabriel'
respuesta = saludar(username)

username = 'Andres'

respuesta()
