from Datos import cargar, guardar

def registrar_adoptante():
    adoptantes = cargar("adoptantes.json")

    dni = input("DNI: ")

    for adoptante in adoptantes:
        if adoptante["dni"] == dni:
            return "Ese DNI ya esta registrado"

    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    localidad = input("Localidad: ")

    adoptante = {
        "dni": dni,
        "nombre": nombre,
        "telefono": telefono,
        "localidad": localidad
    }

    adoptantes.append(adoptante)
    guardar(adoptantes.json, adoptantes)

    print("Adoptante registrado correctamente")

def registrar_adopcion():
    animales = cargar("animales.json")
    adoptantes = cargar("adoptantes.json")
    adopciones = cargar("adopciones.json")

    id_animal = input("Identificador del animal: ")

    animal_encontrado = None

    for animal in animales:
        if animal["id"] == id_animal:
            animal_encontrado = animal
            break

    if animal_encontrado is None:
        print("Animal no encontrado")
        return

    if animal_encontrado["estado"] != "disponible":
        print("El animal no esta disponible para adopcion")
        return

    dni = input("DNI del adoptante: ")

    adoptante_encontrado = False

    for adoptante in adoptantes:
        if adoptante["dni"] == dni:
            adoptante_encontrado = True
            break

    if not adoptante_encontrado:
        return "El adoptante no esta registrado"

    fecha = input("Fecha de adopcion: ")

    adopcion = {
        "animal_id": id_animal,
        "dni_adoptante": dni,
        "fecha": fecha
    }

    adopciones.append(adopcion)

    animal_encontrado["estado"] = "adoptado"

    guardar("animales.json", animales)
    guardar("adopciones.json", adopciones)

    print("Adopcion registrada correctamente")