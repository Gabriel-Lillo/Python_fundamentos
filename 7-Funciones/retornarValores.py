#  Retornar valores  Con la palabra reservada "return"
# Esto nos permite tomar un valor entregado por la funcion y así utilizarlo mas adelante o asignarlo a una variable

def suma(n1, n2): 
    return n1 + n2, 'puede retornar todo tipo de valores como este string' # -> return puede retornar N valores

numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))

resultado, mensaje = suma(numero_uno, numero_dos) 

print('El resultado es: ', resultado)
print(mensaje)


# Otro ejemplo

def suma_2(a, b):
    resultado = a + b 
    return resultado

c = suma_2(1, 2)
b = suma_2(c, 2) #-> Podemos asignar como argumento el mismo valor entregado por la función

print(b)