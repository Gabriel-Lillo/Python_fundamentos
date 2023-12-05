# Los Callback son funciones que son utilizados como argumento para otras funciones.

promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

print(promedio(10, 10, 9, 8, 7))
print(aprobatorio(7))

# En este ejemplo utilizaremos como parametros las dos funciones definidas anteriormente
def mostrar_mensaje(func_promedio, func_abprobatorio, *args): # -> callback
    promedio = func_promedio(*args)

    if func_abprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}')
    else:
        print('No aprobaste la materia.')
    

mostrar_mensaje(promedio, aprobatorio, 10, 10, 8, 7, 7)

'''
Los callback son muy utiles para los programas que son modularizables
'''
