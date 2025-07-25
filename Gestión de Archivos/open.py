from io import open

# Escritura

# texto = "Hola Mundo!"
# archivo = open("Gestión de Archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# Lectura

# archivo = open("Gestión de Archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# Lectura como lista

# archivo = open("Gestión de Archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# With y seek

# with open("Gestión de Archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# Agregar

# archivo = open("Gestión de Archivos/hola-mundo.txt", "a+")
# archivo.write("Chao Mundo!")
# archivo.close()

# Lectura y escritura simultánea

# with open("Gestión de Archivos/hola-mundo.txt", "r+") as archivo:
#     texto = archivo.readlines()
#     archivo.seek(0)
#     texto[0] = "Chanchito feliz la"
#     archivo.writelines(texto)


# Hola Mundo!Chao Mundo!
# Chanchito feliz la
