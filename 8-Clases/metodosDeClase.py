'''
METODOS DE CLASE

* Al igual como existen 2 metodos de atributos (Attrs de clase; attrs de instancia). podemos separar en 
  dos tipos los metodos

Metodo de instancia = Le pertenecen al objeto
Metodo de clase = Le pertenece a la clase

'''
class Circulo:

    pi = 3.141592
    
    @classmethod #-> Devemos utilizar el DECORADOR "@classmethod". Con esto le indicamos a python que es un metodo de clase
    def area(cls, radio): #-> Por convencion el parametro que recive un metodo de clase es "cls"
        return cls.pi * (radio **2)


resultado = Circulo.area(14)
print(resultado)




