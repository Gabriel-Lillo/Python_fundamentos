'''
¿Qué pasa si la funcion a decorar recive argumentos y parametros y retorna algun tipo de valor?
    en esos casos hay que adaptar el decorador apoyandonos con  *args y **kwargs
'''

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs): # la funcion C es la que extiende las funcionalidades!
        print('Nos encontramos en la funcion c')
        print('<<< Antes del llamado >>>')

        resultado = funcion_b(*args, **kwargs) #!!!
        
        print('<<< Despues del llamado >>>')
        return resultado
    return funcion_c


@funcion_a #-> Un decorador se puede usar N cantidad de veces
def suma(numero_1, numero_2):
    return numero_1 + numero_2

resultado = suma(10, 20)
print(resultado)