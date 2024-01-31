import usuarios


# dir() nos enlista metodos magicos y los subpaquetes
# Esto nos sirve para que en el caso tengamos muchos paquetes podamos referenciarlo en distintas partes de nuestra aplicacion.
print(dir(usuarios))

print(usuarios.__name__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__file__)