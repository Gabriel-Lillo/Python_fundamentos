# El operador ternario nos permite reducir lineas de codigo

calificacion = 5


# Operacion normal
color = None

if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'

print(calificacion, color)

# Con operacion ternaria
calificacion = 10

color = 'Verde' if calificacion >= 7 else 'Rojo' # -> En ternario el "else" es obligatorio
print(calificacion,color)