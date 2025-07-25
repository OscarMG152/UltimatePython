cursos = [
    {"nombre": "HTML: Sin Fronteras", "estado": "en progreso"},
    {"nombre": "CSS3: Sin Fronteras", "estado": "completado"},
    {"nombre": "SQL: Sin Fronteras", "estado": "no iniciado"},
    {"nombre": "Python: HTML, CSS, Flask, MySQL", "estado": "en progreso"},
    {"nombre": "Aprende Javascript, HTML5, CSS3 y NodeJS desde cero",
        "estado": "completado"},
    {"nombre": "React - Guía definitiva: hooks, router, redux, next + Proyectos",
        "estado": "no iniciado"},
    {"nombre": "TypeScript: sin fronteras", "estado": "completado"},
    {"nombre": "Ultimate Python", "estado": "en progreso"},
    {"nombre": "Ultimate Linux", "estado": "completado"},
    {"nombre": "Ultimate Docker", "estado": "no iniciado"},
    {"nombre": "Ultimate GIT + GITHUB", "estado": "en progreso"},
    {"nombre": "Ultimate JavaScript", "estado": "completado"},
    {"nombre": "Ultimate React", "estado": "no iniciado"},
    {"nombre": "Ultimate Java", "estado": "en progreso"},]


def filtrar_cursos(cursos):
    en_progreso = filter(
        lambda curso: curso['estado'] == 'en progreso', cursos)
    completados = [
        curso for curso in cursos if curso['estado'] == 'completado']
    no_iniciados = [
        curso for curso in cursos if curso['estado'] == 'no iniciado']
    return en_progreso, completados, no_iniciados


def mostrar_cursos(cursos, titulo):
    print(f"{titulo}:")
    for curso in cursos:
        print(f"- {curso['nombre']}")
    print()


def mostrar_cursos_por_estado(cursos):
    en_progreso, completados, no_iniciados = filtrar_cursos(cursos)

    mostrar_cursos(en_progreso, "Cursos en Progreso")
    mostrar_cursos(completados, "Cursos Completados")
    mostrar_cursos(no_iniciados, "Cursos no Iniciados")


mostrar_cursos_por_estado(cursos)
