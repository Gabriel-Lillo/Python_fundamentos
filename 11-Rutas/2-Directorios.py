from pathlib import Path


path_instancia = Path("11-Rutas")

# path_instancia.exists() #-> Valida si el directorio existe
# path_instancia.mkdir() #-> Creo el directorio
# path_instancia.rmdir() #-> Elimina el directorio
# path_instancia.rename("chanchito-feliz") #-> Cambia el nombre del directorio.



archivos = [p for p in path_instancia.iterdir() if not p.is_dir] #-> Devuelve todos los archivos que no sean directorios.
archivos = [p for p in path_instancia.glob("01-*.py")]
archivos = [p for p in path_instancia.glob("**/*.py")] #-> Devuelve todos los archivo con extencion .py que existen en 11-Rutas
archivos = [p for p in path_instancia.rglob("*.py")] #-> rglob es de recursive. Hace lo mismo que la linea anterior 

print(archivos)
