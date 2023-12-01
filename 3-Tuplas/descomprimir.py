# "Desenpaquetado"

# * -> lista
# _ -> Omitir valor


numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # en el caso que se desconosca la cantidad de elementos en una tupla podemos encasillar el resto en una lista

uno, dos, tres, cuatro, cinco, *resto_valores = numeros # -> * asterisco en variables significa listas 
uno, dos, tres, cuatro, cinco, *_ = numeros # -> en el caso de querer omitir los valores restantes solo se indica *_
uno, _, tres, cuatro, cinco, *_, nueve, diez = numeros # -> Podemos seleccionar los valores que no interesan y omitir el resto


print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(resto_valores)
print(nueve)
print(diez)
