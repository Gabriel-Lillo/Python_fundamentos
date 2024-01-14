""" Comparando objetos """


class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # __eq__ : Esta funcion magica nos permite comparar los valores de dos objetos. (Equal)
    def __eq__(self, otro): 
        return self.lat == otro.lat and self.lon == otro.lon
        
    # __ne__ : Este es otro metodo magico que nos permite comparar (Not Equal)
    def __ne__(self, otro): 
        return self.lat != otro.lat or self.lon != otro.lon
        
    # __lt__ : Este es otro metodo magico para comparar menor que (Less Than)    
    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon
    
    # __le__ : Este es otro metodo magico para comparar menor o igual (Less or Equal)
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon

coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords == coords2) #-> Pese a que ambos tienen los mismos valores, retornará False, ya que lo que se esta evaluando son los espacios en memoria de los objetos, y como estan en distintos espacion de la memoria no son los mismo. para esto es necesario utilizar la funcion magica __eq__
# print(coords != coords2)
print(coords < coords2)
print(coords <= coords2)


