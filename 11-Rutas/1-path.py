from pathlib import Path # La clase Path nos permite referenciar una ruta desde nuestra maquina. (No es necesario que la ruta exista, es solo una referencia)

# r se conoce como "raw string". Se utiliza para escribir \ sin que se considere scape.

# Path(r"C:\Archivos de Programa\Minecraft") #-> Ruta en Windows
# Path("/usr/bin") #-> ruta en linux
# Path()
# Path.home()
# Path("one/__init__.py")


path_instancia = Path("Hola-mundo/mi-archivo.py")

path_instancia.is_file() #-> metodo que sirve para identificar si es una rchivo
path_instancia.is_dir() #-> Metodo para identificar si es un directorio.
path_instancia.exists() #-> Metodo para identificar si existe o no.


"""Tambien path_instancia tendrá acceso a propiedades heredadas de la clase Path"""

print(
    path_instancia.name, #-> Nombre de archivo incluyendo su extencion
    path_instancia.stem, #-> Nombre del archivo sin su extencion
    path_instancia.suffix, #-> La extencion del archivo. ej: .exe , .txt , .py
    path_instancia.parent, #-> De donse se está generando este path. Es este caso sería: hola-mundo
    path_instancia.absolute() #-> Entrega la ruta completa de donde se encuantra el archivo
)

""" Mas metodos para trabajar con Path"""

p = path_instancia.with_name("Chanchito.py") #-> Cambiará el nombre
print(p)
p = path_instancia.with_suffix(".txt") #-> Cambia el sufijo
print(p)
p = path_instancia.with_stem("Feliz.py") #-> Cambia el nombre sin el sufijo
print(p)