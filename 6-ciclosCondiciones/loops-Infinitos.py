""" Loops infinitos """

# Es cuando no tenemos una condición de salida

while True: #-> Esto hace que el loop sea infinito
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break #-> Es importante que al declarar un loop infinito tenga una forma de salida. 

