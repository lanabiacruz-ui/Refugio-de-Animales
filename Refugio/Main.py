from Refugio import registrar, mostrar, buscar, filtrar, mostrar_disponibles, mostrar_adoptados
from Adopciones import registrar_adoptante, registrar_adopcion
from Estadisticas import cantidad, cantidad_de_adopciones, especie_mas_adoptada, edad_promedio_de_adoptados, porcentaje_adoptados


def menu():
    while True:
        print("==== REFUGIO HUELLAS ====")
        print("1. Registrar animal")
        print("2. Consultar animales")
        print("3. Buscar animal")
        print("4. Filtrar por especie")
        print("5. Mostrar animales disponibles")
        print("6. Mostrar animales adoptados")
        print("7. Registrar adoptante")
        print("8. Registrar adopcion")
        print("9. Estadisticas")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar()

        elif opcion == "2":
            mostrar()

        elif opcion == "3":
            buscar()

        elif opcion == "4":
            filtrar()

        elif opcion == "5":
            mostrar_disponibles()

        elif opcion == "6":
            mostrar_adoptados()

        elif opcion == "7":
            registrar_adoptante()

        elif opcion == "8":
            registrar_adopcion()

        elif opcion == "9":
            print("--- ESTADISTICAS ---")
            print("Animales disponibles:", cantidad())
            print("Total de adopciones:", cantidad_de_adopciones())
            print("Especie mas adoptada:", especie_mas_adoptada())
            print("Edad promedio de adoptados:", edad_promedio_de_adoptados())
            print("Porcentaje de adoptados:", porcentaje_adoptados(), "%")

        elif opcion == "0":
            print("Programa finalizado")
            break

        else:
            print("Opcion invalida")


menu()