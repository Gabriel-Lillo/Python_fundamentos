# Es un tipo especial de funcion el cual retorna objetos que facilmente podemos iterar, esto sin que la funcion finalice
'''
    yield
'''


def pares():
    for numero in range(0, 50, 2):
        return numero #-> Ningun codigo despues de la palabra reservada "return" se ejecutará (finaliza la iteracion) 
        print(numero) # -> no se ejecuta

pares()


def pares(): #-> Es Generador por entregar un valor utilizando la palabra reservada "Yield" (Lazy iterator)
    for numero in range(0, 20, 2):
        yield numero # -> La funcion suspende su ejecucion hata que la funcion es nuevamente llamado

        # print('Se reanuda la ejecucion')

for par in pares(): # -> Iteracion que llama N cantidad de veces la "Funcion generador"
    print(par)

'''
La principal ventaja de utilizar funcioness generadoras es que podemos utilizar el valor entregado a demanda 
y no utilizar datos que sabemos que no utilizaremos. tambien ahorrar espacio en memoria

Es recomendable utilizar los generadores cuando se trabaja con cientos o miles de registros
'''

generador = pares()

print(next(generador)) #-> Con la palabra reservada "Next" podemos utilizar los datos entregado por una funcion generador a demanda
print(next(generador))
print(next(generador))

# Otro ejemplo

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo')
        break
