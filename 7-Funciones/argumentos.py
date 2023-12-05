# Funcion para obbtener promedio
'''
El uso de * en un parametro hace referencia a una tupla
'''

def promedio(*listado): # -> Utilizar * en un parametro nos permite crear funciones con n cantidad de argumentos
    print(listado)
    print(type(listado))
    return sum(listado) / len(listado)

resultado = promedio(10, 10, 5, 7, 10) #-> si el parametro de la funcion estuviera sin el * daria error ya que la funcion se le está asignando
                                       # varios argumentos ( resultado = promedio([10, 10, 5, 7, 10]) -> así sería sin * )
print(resultado)


#-> como convencion de python el nombre del parametros con * debe ser asignado como "*args"
def promedio(*args): #-> Tupla
    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)


# El uso del * no impide utilizar otros parametros
def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args) # -> Tupla
    print(p4)

combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, p4=1000)

'''
El uso de ** en un parametro hace referencia a un diccionario (**kwargs)
'''
def usuarios(**kwargs): # -> Diccionario
    print(kwargs)
    print(type(kwargs))

usuarios(gabriel=[10, 10, 8], andres=[10, 9, 9])   


def combinados(p1, p2, *args, **kwargs):
    print(args) #-> tupla
    print(kwargs) #-> diccionario

combinados(1, 2, 3, 4, 5, cody=True, curso='Python')

