# Para generar clase utilizamos la palabra reservada "Class"
'''
Por convencion los nombres de las clases en python se escriben con CamelCase.
otra convencion es que el nombre de la clase se encontrará en singular
'''
# En python no podemos dejar una clase vacia, para evitar un error podemos utilizar la palabra reservada "pass"


class Usuario: #-> definicion de clase
    '''Aqui dentro se ingresan 
    atributos
    y
    metodos'''
    pass

grabriel = Usuario() #-> Instanciamos la clase Usuario a un objeto

print(grabriel)