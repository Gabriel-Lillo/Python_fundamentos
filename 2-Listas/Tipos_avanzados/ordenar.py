

numeros = [2, 4, 1, 45, 75, 22]

numeros.sort()#-> .sort() ordena la lista ya existente
numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True) #-> a diferencia de .sort() este crea una nueva lista

print(numeros)
print(numeros2)


# En el caso de que una lista tenga otras listas o tuplas

usuarios = [
    ["Chanchito", 4],
    ["Gabriel", 1],
    ["Pulga", 5]
]

# def ordena(elemento):
#     return elemento[1] #-> esta funcion lo podemos hacer como expresion lambda

usuarios.sort(key=lambda elemento: elemento[1], reverse=True)
# print(usuarios)