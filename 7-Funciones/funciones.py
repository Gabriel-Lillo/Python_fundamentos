'''
Las funciones en python son "Ciudadanos de primera clase", es decir, las funciones
pueden ser asignadad a variables, como argumentos de otras funciones,
y tambien las funciones pueden retornar otras funciones
'''

def suma(): # -> los nombres de las funciones se escriben con sanake_case
    numero_uno = int(input('Ingresa el primer numero entero: '))
    numero_dos = int(input('Ingresa el segundo numero entero: '))

    resultado = numero_uno + numero_dos
    print(resultado)

suma() #-> la funciones se pueden llamar N cantidad de veces


 # Parametros y Argumantos
def suma(n1, n2): #-> PARAMETROS. En este caso las variables puede venir de cualquier lado
    resultado = n1 + n2
    print(resultado)

numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))

suma(numero_uno, numero_dos) #-> ARGUMENTOS

