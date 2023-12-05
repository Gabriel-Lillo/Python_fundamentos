#  Retornar valores  Con la palabra reservada "return"


def suma(n1, n2): 
    return n1 + n2, 'puede retornar todo tipo de valores como este string' # -> return puede retornar N valores

numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))

resultado, mensaje = suma(numero_uno, numero_dos) 

print('El resultado es: ', resultado)
print(mensaje)
