# Las tuplas son como las listas con la unica diferencia es que son inmutables. No se modificarán durante el programa
# las tuplas de declaran con parentesis normales "()" y son solo para consultas
# Las tuplas son mas rapidas que las listas para consultar


tupla = ('String', 10, 15.4, True, [1, 2, 3], (4, 5, 6))

print(tupla)


# Los indices en tuplas son iguales que las las listas

cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')

primer_cursos = cursos[0]
print(primer_cursos)

ultimo_cursos = cursos[-1]
print(ultimo_cursos)

sub_tupla = cursos[0:3] # -> Las sub tuplas funcionan igual que las sub listas
print(sub_tupla)


# Tambien podemos trasformar una tupla a lista o una lista a tupla con los siguientes metodos:


cursos = ['Python', 'Flask', 'Django']
print(tupla(cursos))

niveles = ('Basico', 'Intermedio', 'Avanzado')
print(list(niveles))


