# Los decoradores nos permite extender funcionalidades a las funciones
'''
# Un decoradores es una funcion que toma como valor de entrada una funcion, y a su vez retorna otra funcion

Al momento de implementar un decorador estaremos trabajando, por lo menos, con tres funciones; el input, el output y la funcion principal
Solemos usar decoradores cuando queremos extender funcionalidades a una funcion (En los casos que no pudamos modificar una funcion)

Ejemplo:

a -> La funcion principal (Decorador)
b -> La funcion a decorar
c -> La funcion decorada 

a(b) -> c
'''
# Estructura
#   Decorador
def funcion_a(funcion_b): # -> funcion a decorar

    def funcion_c(): #-> funcion decorada. la funcion C es la que extiende las funcionalidades!
        print('Nos encontramos en la funcion c')
        print('<<< Antes del llamado >>>')

        funcion_b()
        
        print('<<< Despues del llamado >>>')
        #pass

    return funcion_c

# Ejemplo
@funcion_a # -> Decorador
def saludar():
    print('Hola, nos encontramos en una funcion')

#saludar()

@funcion_a #-> Un decorador se puede usar N cantidad de veces
def suma():
    print(10 + 30)

suma()
'''
¿Qué pasa si la funcion a decorar recive argumentos y parametros y retorna algun tipo de valor?
    en esos casos hay que adaptar el decorador apoyandonos con  *args y **kwargs
'''

