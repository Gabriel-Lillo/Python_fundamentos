""" Como buscar strings dentro de otros strings """

titulo_curso = 'Curso profesional de python'

# Metodo find()
encontrar = titulo_curso.find("de")
print(encontrar) 

# metodo count()
contador = titulo_curso.count('o') # -> retornará la cantidad de coinsidencias
print(contador)

# Utilizando 'in' o "not in"
print('python' in titulo_curso.lower()) #-> da como resultado un valor booleano
print('python' not in titulo_curso.lower()) #-> da como resultado un valor booleano


# metodo .startswith() o .endswith() da como reultado un valor booleano
print(titulo_curso.startswith('Curso'))
print(titulo_curso.endswith('Curso'))

