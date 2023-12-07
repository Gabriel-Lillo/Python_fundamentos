lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']

# [start:end]
# [start:] -> Obtenemos los ultimos elementos de la lista
# [:end] -> Obtendremos los primeros elementos de la lista
# [start:end:skip] -> Obtendremos los elemento con saltos entre los elementos


sub_lista1 = lista_cursos[0:3] # El index final no será incluido en la lista
sub_lista2 = lista_cursos[::-1] # Se obtendrá la lista al inversa
sub_lista3 = lista_cursos[-3:] # retorna una sublista con los ultimos tres elementos de la lista

print(sub_lista1)
print(sub_lista2)
print(sub_lista3)