# Existe metodos para reconoces las llaves y valores 

"""
.keys()
.values()
.items()
"""

diccionario = {'a': 1, 'b': 2,'c': 3,'d': 4}

llaves = tuple(diccionario.keys()) #-> Es recomendable trabajar con tuplas ya que estos metodos retornan un objeto
print(llaves)

values = tuple(diccionario.values()) #-> Es recomendable trabajar con tuplas ya que estos metodos retornan un objeto
print(values)

elementos = tuple(diccionario.items())
print(elementos)