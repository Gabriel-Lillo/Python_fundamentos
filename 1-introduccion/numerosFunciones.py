import math #-> Modulo math

"""El modulo math tiene muchos metodos 
pero estos son lo mas importantes

para ver todos los metodos que contiene en modulo mas 
lo encontraremos buscando en el navegados : python math
"""
print(math.ceil(1.1)) #-> devolverá el numero entero mas cercano hacia arriba (resultado = 2)
print(math.floor(1.999999)) #-> Devolverá el numero entero mas cercano hacia abajo (resultado = 1)
print(math.isnan(23)) #-> Devolverá un valor booleano en el caso de que el valor sea un numero. solo sirve con numeros (resultado = False)
print(math.pow(10, 3)) #-> Nos permite elevar un numero a una potencia de algo.
print(math.sqrt(9)) #-> Nos permite sacar la raiz cuadrada de un numero



# round() -> Devolverá el numero entero al cual este mas cercano
print(round(1.3)) #-> devolvrá 1.
print(round(1.7)) #-> devolverá 2
print(round(1.5)) #-> devolverá 2


# abs() -> Devolverá el valor absoluto. Siempre entregará un numero positivo
print(abs(-77))
print(abs(55))

