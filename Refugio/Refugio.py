from Datos import cargar, guardar

def registrar():
    animales = cargar("animales.json")
    identificador = len(animales) + 1

    nombre = input("Nombre: ")
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    edad = int(input("Edad aproximada: "))

    if edad < 0:
        return "La edad no puede ser negativa"
    sexo = input("Sexo: ")
    salud = input("Estado de salud: ")
    animal = {
        "id": identificador,
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "sexo": sexo,
        "salud": salud,
        "estado": "disponible"
    }
    animales.append(animal)
    guardar("animales.json", animales)
    print("Animal registrado correctamente")

def mostrar():
    animales = cargar("animales.json")
    if len(animales) == 0:
        return "No hay animales registrados"
    for animal in animales:
        print(animal)

def buscar():
    animales = cargar("animales.json")
    busqueda = input("Ingrese nombre o identificador: ")
    for animal in animales:
        if animal["id"] == busqueda or animal["nombre"].lower() == busqueda.lower():
            return animal
    print("Animal no encontrado")

def filtrar():
    animales = cargar("animales.json")
    especie = input("Ingrese la especie: ")
    encontrados = False
    for animal in animales:
        if animal["especie"].lower() == especie.lower():
            print(animal)
            encontrados = True
    if not encontrados:
        print("No hay animales de esa especie")

def mostrar_disponibles():
    animales = cargar("animales.json")
    for animal in animales:
        if animal["estado"] == "disponible":
            print(animal)

def mostrar_adoptados():
    animales = cargar("animales.json")

    for animal in animales:
        if animal["estado"] == "adoptado":
            print(animal)

