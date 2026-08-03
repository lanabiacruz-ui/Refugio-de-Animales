import os
os.system("cls")
def main

while True:
    print("--- MENU ---")
    print("1- Registrar Animales")
    print("2- Consultar por Animales")
    print("3- Buscar por nombre o identificador")
    print("4- Filtrar Animales")
    opc = input("Ingrese una opcion: ")
    if opc == "1":
        Dicc = {}
       
        Name = input("Ingrese el nombre del animal: ")
        Esp = input("Ingrese el tipo de especie: ")
        Sexo = input("Ingrese el sexo del animal: ")
        Edad = input("Ingrese su edad: ")
        Salud = input("")