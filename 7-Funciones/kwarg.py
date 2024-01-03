""" Keyword Argument """

def get_product(**datos): #-> Los kwarg se definen con **
    print(datos["id"], datos["name"]) #-> Siqueremos acceder a un dato en especifico utilizamos []

get_product(id="23", 
            name="iPhone", 
            descr="Esto es un iphon") #-> Siempre que se llame a una funcion con kwarg, hay que indicar el nombre del parametro


# Podemos usar todos los argumentos que queramos y serán entregados como diccionario

