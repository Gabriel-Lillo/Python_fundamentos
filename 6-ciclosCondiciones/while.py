# While nos permite repetir codigo N cantidad de veces hasta que la condición deje de cumplirse


contador =1

while contador <= 10:
    print(contador)
    contador = contador + 1


# Mejor ejemplo
numero = 1234
contador_digitos = 0

while numero >= 1:
    #contador_digitos = contador_digitos + 1
    contador_digitos +=1 #-> Esto es lo mismo que la linea 16 pero mas corto
    numero = numero / 10
else: # -> else es opcional, pero se puede usar con while
    print('Fin del ciclo while')

print(contador_digitos)

# El ciclo while solo lo utilizaremos condo no sabemos cuantas iteraciones vamos a realizar