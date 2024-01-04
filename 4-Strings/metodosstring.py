""" Un metodo es una funcion que pertenece a un objeto """

animal = "  chanCHito feliz  "

print(animal.upper()) # -> tranfoma todas las letras en mayuscula
print(animal.lower()) # - > tranfoma todas las letras en minuscula
print(animal.strip()) # -> Este metodo eliminará los espacios existentes a la izquierda y derecha
print(animal.capitalize()) # -> tranfoma la primera letra en mayuscula dejando el resto en minuscula
print(animal.title()) # -> transforma la primera letra de cada palabra en mayuscula y el resto lo deja en minuscula
print(animal.find("cH")) # -> Retornará un numero positivo segun el indice, de lo contrario entregará -1 (no lo encontró)
print(animal.replace("nCh", "j")) # -> Si o si recive como parametro un valor existente y el valor que reemplazará

# * los metodos pueden ser encadenados Ejemplo : print(animal.strip().capitalize())