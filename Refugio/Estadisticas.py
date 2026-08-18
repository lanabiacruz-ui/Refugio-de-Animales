from Datos import cargar

def cantidad():
    animales = cargar("animales.json")
    cantidad = 0
    for animal in animales:
        if animal["estado"] == "disponible":
            cantidad += 1
    return cantidad

def cantidad_adopciones():
    adopciones = cargar("adopciones.json")
    return len(adopciones)

def especie_mas_adoptada():
    animales = cargar("animales.json")
    especies = {}
    for animal in animales:
        if animal["estado"] == "adoptado":
            especie = animal["especie"]

            if especie not in especies:
                especies[especie] = 0

            especies[especie] += 1

    if len(especies) == 0:
        return "No hay adopciones"

    return max(especies, key=especies.get)

def edad_promedio_adoptados():
    animales = cargar("animales.json")

    edades = []

    for animal in animales:
        if animal["estado"] == "adoptado":
            edades.append(animal["edad"])

    if len(edades) == 0:
        return 0

    return sum(edades) / len(edades)

def porcentaje_adoptados():
    animales = cargar("animales.json")

    if len(animales) == 0:
        return 0

    adoptados = 0

    for animal in animales:
        if animal["estado"] == "adoptado":
            adoptados += 1

    return (adoptados / len(animales)) * 100