titulo_curso = 'Curso profesional de Python'


for caracter in titulo_curso:
    if caracter == 'P':
          break #-> detiene la iteracion 
    
    print(caracter)



for caracter in titulo_curso:
    if caracter == ' ':
          continue #-> esta instruccion hará que se salten los espacios o cualquier elemento que se especifique en if
          # Continua la iteracion
    print(caracter)