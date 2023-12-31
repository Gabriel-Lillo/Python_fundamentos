

int() #-> Convierte cualquier tipo de dato a numero entero
str() #-> Convierte cualquier tipo de dato a string
float() #-> Convierte cualquier tipo de dato a un numero decimal
bool() #-> Convierte cualquier tipo de dato a un booleano

""" 
En python existen dos terminos
que tienen que ver con la funcion bool()

Truthy:
    Elementos True

Falsy: 
    ""
    0
    None

* bool() solo entregará False con cualquiera de los tres casos Falsy     
"""

print(bool("")) #-> False
print(bool("0")) #-> True
print(bool(None)) #-> False
print(bool(" ")) #-> True
print(bool(0)) #-> False