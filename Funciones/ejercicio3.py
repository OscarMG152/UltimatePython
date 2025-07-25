def a_segundos(cantidad, unidad):
    if unidad == 'segundo':
        return cantidad
    elif unidad == 'minuto':
        return cantidad * 60
    elif unidad == 'hora':
        return cantidad * 3600
    elif unidad == 'dia':
        return cantidad * 86400
    elif unidad == 'mes':
        return cantidad * 2592000
    elif unidad == 'año':
        return cantidad * 31536000
    else:
        return 'Error'


def de_segundos(cantidad, unidad):
    if unidad == 'segundo':
        return cantidad
    elif unidad == 'minuto':
        return cantidad / 60
    elif unidad == 'hora':
        return cantidad / 3600
    elif unidad == 'dia':
        return cantidad / 86400
    elif unidad == 'mes':
        return cantidad / 2592000
    elif unidad == 'año':
        return cantidad / 31536000
    else:
        return 'Error'


def convertir_tiempo(cantidad, origen, destino):
    cantidad_en_segundos = a_segundos(cantidad, origen)
    if cantidad_en_segundos == 'Error':
        print('Unidad de tiempo no válida')
    cantidad_convertida = de_segundos(cantidad_en_segundos, destino)
    return f"{cantidad} {origen}(s) es igual a {cantidad_convertida} {destino}(s)"


print(convertir_tiempo(2, 'hora', 'minuto'))
