lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos2 = ['C', 'C++', 'Docker']

print(len(lista_cursos)) # len() sirve para conocer  la cantidad de elementos en la lista 


# .appedn() Sirve para agregar un elemento ala final de la lista

lista_cursos.append('MongoDB')
lista_cursos.append('C#')
print(lista_cursos)

# .insert() Sirve para insertar un elemento en un indice especifico en la lista

lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'Pygame')
print(lista_cursos)

# .extend() Sirve para extender una lista con elementos de otra lista

lista_cursos.extend(lista_cursos2)
print(lista_cursos)


# .remove() o "del" Sirven para eliminar un elemento especifico de la lista

lista_cursos.remove('MongoDB')
print(lista_cursos)
del lista_cursos[0]
print(lista_cursos)


# .clear() Dejerá la lista totalmente vacía

lista_cursos.clear()
print(lista_cursos)
