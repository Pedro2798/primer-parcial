# Menú principal para la competencia de baile

from funciones import *

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Participantes con promedio menor a 4")
    print("5. Participantes con promedio menor a 8")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Jurado más generoso")
    print("9. Participantes con puntuaciones iguales")
    print("10. Buscar participante por nombre")
    print("11. Mostrar top 3 participantes con mejor promedio")
    print("12. Mostrar participantes ordenados por promedio")
    print("0. Salir")

# Estructura de datos inicial (vacía)
nombres = ["", "", "", "", ""]
puntajes_j1 = [0, 0, 0, 0, 0]
puntajes_j2 = [0, 0, 0, 0, 0]
puntajes_j3 = [0, 0, 0, 0, 0]

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "0":
        print("¡Hasta luego!")
        break
    elif opcion == "1":
        cargar_participantes(nombres)
    elif opcion == "2":
        cargar_puntuaciones(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "3":
        mostrar_puntuaciones(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "4":
        mostrar_promedio_menor_4(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "5":
        mostrar_promedio_menor_8(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "6":
        mostrar_promedio_jurado(puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "7":
        mostrar_jurado_estricto(puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "8":
        mostrar_jurado_generoso(puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "9":
        mostrar_puntajes_iguales(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "10":
        buscar_participante(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "11":
        mostrar_top3_promedio(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "12":
        mostrar_participantes_ordenados(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    else:
        print("Opción inválida. Intente nuevamente.")
