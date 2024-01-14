""" Else y finally """

# Else : Se utiliza cuando queremos agregar otro bloque de codigo pero solamente cuando no haya ocurrido ningun error y queremos mantenernos dentro del contexto de try except 
# Finally : Se utiliza independiente si existe error o no

try:
    n1 = int(input("Ingresa primer número"))
except Exception as e:
    print("Ha ocurrido una error")
else: #-> Esete bloque se ejecutará solo si no ha ocurrido ninguna excepcion/error
    print("No ocurrio ningun error")
finally: #-> Este bloque se ejecuta independientemente que exista error o no
    print("Se ejecuta siempre")