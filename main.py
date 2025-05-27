# Menú principal para la competencia de baile

from funciones import *
from Inputs import input_opcion_menu

def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Participantes con promedio menor a 4")
    print("5. Participantes con promedio menor a 8")
    print("6. Promedio de cada jurado")
    print("7. Jurado mas estricto")
    print("8. Jurado mas generoso")
    print("9. Participantes con puntuaciones iguales")
    print("10. Buscar participante por nombre")
    print("11. Mostrar top 3 participantes con mejor promedio")
    print("12. Mostrar participantes ordenados alfabeticamente")
    print("0. Salir")

nombres = [""] * 5
puntajes_j1 = [0] * 5
puntajes_j2 = [0] * 5
puntajes_j3 = [0] * 5
participantes_cargados = False
puntajes_cargados = False

while True:
    mostrar_menu()
    opcion = input_opcion_menu("Seleccione una opcion: ", [str(i) for i in range(13)])
    if opcion == "0":
        print("¡Hasta luego!")
        break
    elif opcion == "1":
        participantes_cargados = cargar_participantes(nombres)
        puntajes_cargados = False
    elif opcion == "2":
        if not participantes_cargados:
            print("Primero debe cargar los participantes.")
        else:
            puntajes_cargados = cargar_puntuaciones(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "3":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            mostrar_puntuaciones(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "4":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            mostrar_promedio_menor(nombres, puntajes_j1, puntajes_j2, puntajes_j3, 4)
    elif opcion == "5":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            mostrar_promedio_menor(nombres, puntajes_j1, puntajes_j2, puntajes_j3, 8)
    elif opcion == "6":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            mostrar_promedio_jurado(puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "7":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            mostrar_jurado_estricto(puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "8":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            mostrar_jurado_generoso(puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "9":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            mostrar_puntajes_iguales(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "10":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            buscar_participante(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "11":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            mostrar_top3_promedio(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
    elif opcion == "12":
        if not (participantes_cargados and puntajes_cargados):
            print("Debe cargar participantes y puntajes primero.")
        else:
            mostrar_participantes_ordenados(nombres, puntajes_j1, puntajes_j2, puntajes_j3)
