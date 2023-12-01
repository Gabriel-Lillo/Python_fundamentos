lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

# Con la funcion zip() podremos unir los valores de la tupla y de la lista

resultado = zip(tupla, lista) # -> entrega un objeto en formato zip
resultado = tuple(resultado)
# resultado = list(resultado)

print(resultado)


# si una tupla o lista tiene mas elementos que el resto, esos datos serán omitidos.
