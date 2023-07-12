# Manipulación de archivos

# ABRIR ARCHIVOS ----------------------------------------------------------

# Abrir archivos
c = open("./lorem.txt")
# Permisos para abrir un archivo (segundo argumento de read())
# "r" para read
# "a" para append
# "w" para escribir
# "x" para crear archivos (si el archivo existe, se genera un error)

# Lee todo el texto
# print(c.read())

# Para leer cada líena del archivo
# print(c.readline())

# Para leer las líneas con iteración
for x in c:
    print(x)

# Para cerrar el archivo
c.close()

# -------------------------------------------------------------------------
# Abrir archivo con parámetro de 'append', al final
d = open("./ipsum.txt", "a")

# Agregaremos una nueva línea al archivo
d.write("\nNueva línea al texto al final del texto")

# Para cerrar el archivo
d.close()

# -------------------------------------------------------------------------

# Abrir archivo con parámetro de 'write', reemplazamos todo
e = open("./ipsum.txt", "w")

# Agregaremos una nueva línea al archivo
e.write("Línea que reemplaza todo el texto")

# Para cerrar el archivo
e.close()

# -------------------------------------------------------------------------

# Eliminar archivos y carpetas
import os

# os.remove("./gestion_archivos/ipsum.txt")

# Eliminar con condicional según existencia del archivo
if os.path.exists("./dummy.txt"):
    os.remove("./dummy.txt")
else:
    print("El archivo no existe")

# Para eliminar carpeta
os.rmdir("./directorio_dummy")
