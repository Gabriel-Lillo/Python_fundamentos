nombre  = 'Gabriel Andres'
apellido = 'Lillo'

nombre_completo = 'Mr.' + nombre + " " + apellido

print(nombre_completo)

# otra forma de concatenar es:  %s
#                      1  2  3  	 1         2         3
nombre_completo = 'Mr. %s %s %s' %(nombre, apellido, 'Pepito')

print(nombre_completo)

# Otra forma de concatenar es: {} "placeholder"" con metodo .format()
# con los {} podemos definir el orden del string

nombre_completo = 'Mr. {primer_apellido} {segundo_apellido} {nombre}'.format(
    nombre = nombre, 
    primer_apellido = apellido,
    segundo_apellido = 'Vega'
)

print(nombre_completo)

#otra forma de concatenar: F String (interpolacion)

nombre_completo = f'Mr. {nombre} {apellido} {'cualquier cosa'}'

print(nombre_completo)