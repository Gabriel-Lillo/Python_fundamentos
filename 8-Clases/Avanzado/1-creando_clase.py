

class Perro: #-> Para declarar una clase el nombre debe empezar con mayuscula y convencion UpperCamelCase. Esto es para diferenciarlas de las funciones
    def habla(self): #-> Cuando una funcion se encuantra dentro de una clase se pasa a llamar "METODO"
        print("Guau!")


mi_perro = Perro()
mi_perro.habla()

# Para identificar si un objeto es una istancia de una clase utilizamos "isinstance()"
print(isinstance(mi_perro, Perro)) #-> recibe como argumento (objeto, clase). Devuelve un valor booleano
