lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']

# [start:end]
# [start:] -> Obtenemos los ultimos elementos de la lista
# [:end] -> Obtendremos los primeros elementos de la lista
# [start:end:skip] -> Obtendremos los elemento con saltos entre los elementos


sub_lista = lista_cursos[0:3] # El index final no será incluido en la lista
sub_lista = lista_cursos[::-1] # Se obtendrá la lista al inversa

print(sub_lista)