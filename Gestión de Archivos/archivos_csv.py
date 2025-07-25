import csv
import os

# Escribir

# with open("Gestión de Archivos/archivo.csv", "w", newline="") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "Un twit"])
#     writer.writerow([1001, 2, "Otro twit"])

# Leer

# with open("Gestión de Archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# Actualizar

with open("Gestión de Archivos/archivo.csv") as r, open("Gestión de Archivos/archivo_temp.csv", "w", newline="") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "Texto modificado"])
        else:
            writer.writerow(linea)

os.remove("Gestión de Archivos/archivo.csv")
os.rename("Gestión de Archivos/archivo_temp.csv",
          "Gestión de Archivos/archivo.csv")
