from Inputs import input_entero, input_string

def es_nombre_valido(nombre):
    # Verifica que el nombre tenga al menos 3 caracteres y solo letras y espacios
    if len(nombre) < 3:
        return False
    i = 0
    while i < len(nombre):
        c = nombre[i]
        if not ((c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') or c == ' '):
            return False
        i = i + 1
    return True

def cargar_participantes(nombres):
    """
    Carga los nombres de los participantes en la lista nombres.
    Devuelve True si se cargaron correctamente.
    """
    print("\n--- CARGA DE PARTICIPANTES ---")
    for i in range(len(nombres)):
        nombre = input_string(f"Ingrese el nombre del participante {i+1}: ", min_len=3, solo_letras_espacios=True)
        nombres[i] = nombre
    return True

def cargar_puntuaciones(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Carga las puntuaciones de los jurados para cada participante.
    Devuelve True si se cargaron correctamente.
    """
    print("\n--- CARGA DE PUNTUACIONES ---")
    for i in range(len(nombres)):
        if nombres[i] == "":
            print(f"Participante {i+1} no cargado. Salteando.")
            continue
        print(f"Participante: {nombres[i]}")
        puntajes_j1[i] = input_entero("Ingrese puntaje del jurado 1 (1-10): ", 1, 10)
        puntajes_j2[i] = input_entero("Ingrese puntaje del jurado 2 (1-10): ", 1, 10)
        puntajes_j3[i] = input_entero("Ingrese puntaje del jurado 3 (1-10): ", 1, 10)
    return True

def calcular_promedio(a, b, c):
    """
    Calcula el promedio de tres valores numéricos.
    """
    return (a + b + c) / 3.0

def mostrar_puntuaciones(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Muestra los datos y promedios de todos los participantes.
    """
    print("\n--- PUNTUACIONES DE PARTICIPANTES ---")
    for i in range(len(nombres)):
        if nombres[i] != "":
            print("| NOMBRE PARTICIPANTE: ", nombres[i])
            print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
            print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
            print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
            promedio = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
            print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
            print()

def mostrar_promedio_menor(nombres, puntajes_j1, puntajes_j2, puntajes_j3, limite):
    """
    Muestra los participantes cuyo promedio es menor al límite dado.
    Devuelve True si hay al menos uno, False si no hay.
    """
    hay_menor = False
    for i in range(len(nombres)):
        if nombres[i] != "":
            promedio = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
            if promedio < limite:
                hay_menor = True
                print("| NOMBRE PARTICIPANTE: ", nombres[i])
                print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
                print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
                print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
                print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
                print()
    if not hay_menor:
        print(f"No hay participantes con promedio menor a {limite}.")
    return hay_menor

def promedios_jurados(puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Devuelve una tupla con los promedios de cada jurado.
    """
    suma1 = suma2 = suma3 = 0
    for i in range(len(puntajes_j1)):
        suma1 += puntajes_j1[i]
        suma2 += puntajes_j2[i]
        suma3 += puntajes_j3[i]
    return (suma1/len(puntajes_j1), suma2/len(puntajes_j2), suma3/len(puntajes_j3))

def mostrar_promedio_jurado(puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Muestra el promedio de cada jurado.
    """
    p1, p2, p3 = promedios_jurados(puntajes_j1, puntajes_j2, puntajes_j3)
    print(f"Jurado 1: {p1:.2f}/10")
    print(f"Jurado 2: {p2:.2f}/10")
    print(f"Jurado 3: {p3:.2f}/10")

def mostrar_jurado_estricto(puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Muestra todos los jurados con el promedio más bajo.
    """
    p1, p2, p3 = promedios_jurados(puntajes_j1, puntajes_j2, puntajes_j3)
    min_prom = min(p1, p2, p3)
    jurados = []
    if p1 == min_prom:
        jurados.append(1)
    if p2 == min_prom:
        jurados.append(2)
    if p3 == min_prom:
        jurados.append(3)
    # Concatenar jurados manualmente
    jurados_str = ""
    i = 0
    while i < len(jurados):
        jurados_str = jurados_str + str(jurados[i])
        if i < len(jurados) - 1:
            jurados_str = jurados_str + ", "
        i = i + 1
    print("Jurado(s) mas estricto(s): " + jurados_str + f" con promedio {min_prom:.2f}/10")

def mostrar_jurado_generoso(puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Muestra todos los jurados con el promedio más alto.
    """
    p1, p2, p3 = promedios_jurados(puntajes_j1, puntajes_j2, puntajes_j3)
    max_prom = max(p1, p2, p3)
    jurados = []
    if p1 == max_prom:
        jurados.append(1)
    if p2 == max_prom:
        jurados.append(2)
    if p3 == max_prom:
        jurados.append(3)
    # Concatenar jurados manualmente
    jurados_str = ""
    i = 0
    while i < len(jurados):
        jurados_str = jurados_str + str(jurados[i])
        if i < len(jurados) - 1:
            jurados_str = jurados_str + ", "
        i = i + 1
    print("Jurado(s) mas generoso(s): " + jurados_str + f" con promedio {max_prom:.2f}/10")

def mostrar_puntajes_iguales(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Muestra los participantes que recibieron la misma puntuación de los tres jurados.
    Devuelve True si hay al menos uno, False si no hay.
    """
    hay_iguales = False
    for i in range(len(nombres)):
        if nombres[i] != "" and puntajes_j1[i] == puntajes_j2[i] == puntajes_j3[i]:
            hay_iguales = True
            print("| NOMBRE PARTICIPANTE: ", nombres[i])
            print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
            print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
            print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
            promedio = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
            print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
            print()
    if not hay_iguales:
        print("No hay participantes con puntajes iguales entre los tres jurados.")
    return hay_iguales

def buscar_participante(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Permite buscar un participante por nombre y muestra sus datos si existe.
    Devuelve True si lo encuentra, False si no.
    """
    nombre_buscar = input_string("Ingrese el nombre a buscar: ", min_len=3, solo_letras_espacios=True)
    for i in range(len(nombres)):
        if nombres[i] == nombre_buscar:
            print("| NOMBRE PARTICIPANTE: ", nombres[i])
            print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
            print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
            print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
            promedio = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
            print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
            print()
            return True
    print("No existe un participante con ese nombre.")
    return False

def mostrar_top3_promedio(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Muestra los tres participantes con mayor puntaje promedio.
    """
    promedios = [calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i]) if nombres[i] != "" else -1 for i in range(len(nombres))]
    indices = sorted(range(len(promedios)), key=lambda i: promedios[i], reverse=True)
    count = 0
    for idx in indices:
        if nombres[idx] != "" and count < 3:
            print("| NOMBRE PARTICIPANTE: ", nombres[idx])
            print("| PUNTAJE JURADO 1: ", puntajes_j1[idx])
            print("| PUNTAJE JURADO 2: ", puntajes_j2[idx])
            print("| PUNTAJE JURADO 3: ", puntajes_j3[idx])
            print(f"| PUNTAJE PROMEDIO: {promedios[idx]:.2f}/10")
            print()
            count += 1
    if count == 0:
        print("No hay participantes cargados.")

def mostrar_participantes_ordenados(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    """
    Muestra los participantes ordenados alfabéticamente (A-Z) con sus datos.
    """
    datos = [(nombres[i], puntajes_j1[i], puntajes_j2[i], puntajes_j3[i]) for i in range(len(nombres)) if nombres[i] != ""]
    datos.sort(key=lambda x: x[0])
    if not datos:
        print("No hay participantes cargados.")
        return
    for nombre, p1, p2, p3 in datos:
        print("| NOMBRE PARTICIPANTE: ", nombre)
        print("| PUNTAJE JURADO 1: ", p1)
        print("| PUNTAJE JURADO 2: ", p2)
        print("| PUNTAJE JURADO 3: ", p3)
        promedio = calcular_promedio(p1, p2, p3)
        print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
        print() 