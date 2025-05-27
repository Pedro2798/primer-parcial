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
    print("\n--- CARGA DE PARTICIPANTES ---")
    i = 0
    while i < len(nombres):
        nombre = input(f"Ingrese el nombre del participante {i+1}: ")
        if es_nombre_valido(nombre):
            nombres[i] = nombre
            i = i + 1
        else:
            print("Nombre inválido. Debe tener al menos 3 caracteres y solo letras y espacios.")

def cargar_puntuaciones(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    print("\n--- CARGA DE PUNTUACIONES ---")
    i = 0
    while i < len(nombres):
        if nombres[i] == "":
            print(f"Participante {i+1} no cargado. Salteando.")
            i = i + 1
            continue
        print(f"Participante: {nombres[i]}")
        # Jurado 1
        while True:
            try:
                p1 = int(input("Ingrese puntaje del jurado 1 (1-10): "))
                if p1 >= 1 and p1 <= 10:
                    puntajes_j1[i] = p1
                    break
                else:
                    print("Puntaje invalido. Debe ser entre 1 y 10.")
            except:
                print("Debe ingresar un numero entero.")
        # Jurado 2
        while True:
            try:
                p2 = int(input("Ingrese puntaje del jurado 2 (1-10): "))
                if p2 >= 1 and p2 <= 10:
                    puntajes_j2[i] = p2
                    break
                else:
                    print("Puntaje invalido. Debe ser entre 1 y 10.")
            except:
                print("Debe ingresar un numero entero.")
        # Jurado 3
        while True:
            try:
                p3 = int(input("Ingrese puntaje del jurado 3 (1-10): "))
                if p3 >= 1 and p3 <= 10:
                    puntajes_j3[i] = p3
                    break
                else:
                    print("Puntaje invalido. Debe ser entre 1 y 10.")
            except:
                print("Debe ingresar un numero entero.")
        i = i + 1 

def calcular_promedio(a, b, c):
    return (a + b + c) / 3.0

def mostrar_puntuaciones(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    print("\n--- PUNTUACIONES DE PARTICIPANTES ---")
    i = 0
    while i < len(nombres):
        if nombres[i] != "":
            print("| NOMBRE PARTICIPANTE: ", nombres[i])
            print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
            print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
            print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
            promedio = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
            print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
            print()
        i = i + 1 

def mostrar_promedio_menor_4(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    print("\n--- PARTICIPANTES CON PROMEDIO MENOR A 4 ---")
    hay_menor = False
    i = 0
    while i < len(nombres):
        if nombres[i] != "":
            promedio = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
            if promedio < 4:
                hay_menor = True
                print("| NOMBRE PARTICIPANTE: ", nombres[i])
                print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
                print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
                print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
                print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
                print()
        i = i + 1
    if not hay_menor:
        print("No hay participantes con promedio menor a 4.") 

def mostrar_promedio_menor_8(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    print("\n--- PARTICIPANTES CON PROMEDIO MENOR A 8 ---")
    hay_menor = False
    i = 0
    while i < len(nombres):
        if nombres[i] != "":
            promedio = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
            if promedio < 8:
                hay_menor = True
                print("| NOMBRE PARTICIPANTE: ", nombres[i])
                print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
                print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
                print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
                print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
                print()
        i = i + 1
    if not hay_menor:
        print("No hay participantes con promedio menor a 8.") 

def mostrar_promedio_jurado(puntajes_j1, puntajes_j2, puntajes_j3):
    print("\n--- PROMEDIO DE CADA JURADO ---")
    # Calcular promedio jurado 1
    suma1 = 0
    suma2 = 0
    suma3 = 0
    i = 0
    while i < len(puntajes_j1):
        suma1 = suma1 + puntajes_j1[i]
        suma2 = suma2 + puntajes_j2[i]
        suma3 = suma3 + puntajes_j3[i]
        i = i + 1
    promedio1 = suma1 / len(puntajes_j1)
    promedio2 = suma2 / len(puntajes_j2)
    promedio3 = suma3 / len(puntajes_j3)
    print(f"Jurado 1: {promedio1:.2f}/10")
    print(f"Jurado 2: {promedio2:.2f}/10")
    print(f"Jurado 3: {promedio3:.2f}/10") 

def mostrar_jurado_estricto(puntajes_j1, puntajes_j2, puntajes_j3):
    suma1 = 0
    suma2 = 0
    suma3 = 0
    i = 0
    while i < len(puntajes_j1):
        suma1 = suma1 + puntajes_j1[i]
        suma2 = suma2 + puntajes_j2[i]
        suma3 = suma3 + puntajes_j3[i]
        i = i + 1
    promedio1 = suma1 / len(puntajes_j1)
    promedio2 = suma2 / len(puntajes_j2)
    promedio3 = suma3 / len(puntajes_j3)
    min_prom = promedio1
    jurado = 1
    if promedio2 < min_prom:
        min_prom = promedio2
        jurado = 2
    if promedio3 < min_prom:
        min_prom = promedio3
        jurado = 3
    print(f"El jurado mas estricto es el Jurado {jurado} con promedio {min_prom:.2f}/10")

def mostrar_jurado_generoso(puntajes_j1, puntajes_j2, puntajes_j3):
    suma1 = 0
    suma2 = 0
    suma3 = 0
    i = 0
    while i < len(puntajes_j1):
        suma1 = suma1 + puntajes_j1[i]
        suma2 = suma2 + puntajes_j2[i]
        suma3 = suma3 + puntajes_j3[i]
        i = i + 1
    promedio1 = suma1 / len(puntajes_j1)
    promedio2 = suma2 / len(puntajes_j2)
    promedio3 = suma3 / len(puntajes_j3)
    max_prom = promedio1
    jurado = 1
    if promedio2 > max_prom:
        max_prom = promedio2
        jurado = 2
    if promedio3 > max_prom:
        max_prom = promedio3
        jurado = 3
    print(f"El jurado mas generoso es el Jurado {jurado} con promedio {max_prom:.2f}/10")

def mostrar_puntajes_iguales(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    print("\n--- PARTICIPANTES CON PUNTAJES IGUALES ENTRE JURADOS ---")
    hay_iguales = False
    i = 0
    while i < len(nombres):
        if nombres[i] != "":
            # Puntajes iguales entre los tres jurados
            if puntajes_j1[i] == puntajes_j2[i] and puntajes_j2[i] == puntajes_j3[i]:
                hay_iguales = True
                print("| NOMBRE PARTICIPANTE: ", nombres[i])
                print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
                print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
                print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
                promedio = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
                print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
                print()
        i = i + 1
    if not hay_iguales:
        print("No hay participantes con puntajes iguales entre los tres jurados.") 

def buscar_participante(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    nombre_buscar = input("Ingrese el nombre a buscar: ")
    encontrado = False
    i = 0
    while i < len(nombres):
        if nombres[i] == nombre_buscar:
            encontrado = True
            print("| NOMBRE PARTICIPANTE: ", nombres[i])
            print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
            print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
            print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
            promedio = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
            print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
            print()
        i = i + 1
    if not encontrado:
        print("No existe un participante con ese nombre.") 

def mostrar_top3_promedio(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    print("\n--- TOP 3 PARTICIPANTES CON MAYOR PROMEDIO ---")
    promedios = [0] * len(nombres)
    i = 0
    while i < len(nombres):
        if nombres[i] != "":
            promedios[i] = calcular_promedio(puntajes_j1[i], puntajes_j2[i], puntajes_j3[i])
        else:
            promedios[i] = -1  # Para que los vacíos queden al final
        i = i + 1
    # Ordenar índices por promedio descendente
    indices = [0,1,2,3,4]
    j = 0
    while j < len(indices)-1:
        k = j+1
        while k < len(indices):
            if promedios[indices[k]] > promedios[indices[j]]:
                aux = indices[j]
                indices[j] = indices[k]
                indices[k] = aux
            k = k + 1
        j = j + 1
    count = 0
    idx = 0
    while count < 3 and idx < len(indices):
        i = indices[idx]
        if nombres[i] != "":
            print("| NOMBRE PARTICIPANTE: ", nombres[i])
            print("| PUNTAJE JURADO 1: ", puntajes_j1[i])
            print("| PUNTAJE JURADO 2: ", puntajes_j2[i])
            print("| PUNTAJE JURADO 3: ", puntajes_j3[i])
            print(f"| PUNTAJE PROMEDIO: {promedios[i]:.2f}/10")
            print()
            count = count + 1
        idx = idx + 1
    if count == 0:
        print("No hay participantes cargados.")

def mostrar_participantes_ordenados(nombres, puntajes_j1, puntajes_j2, puntajes_j3):
    print("\n--- PARTICIPANTES ORDENADOS ALFABETICAMENTE (A-Z) ---")
    # Copiar datos a nuevas listas para no modificar las originales
    nombres_copia = [nombres[i] for i in range(len(nombres))]
    p1_copia = [puntajes_j1[i] for i in range(len(nombres))]
    p2_copia = [puntajes_j2[i] for i in range(len(nombres))]
    p3_copia = [puntajes_j3[i] for i in range(len(nombres))]
    # Ordenar usando burbuja
    i = 0
    while i < len(nombres_copia)-1:
        j = i+1
        while j < len(nombres_copia):
            if nombres_copia[j] != "" and (nombres_copia[i] == "" or nombres_copia[j] < nombres_copia[i]):
                # Intercambiar todos los datos
                aux_nombre = nombres_copia[i]
                nombres_copia[i] = nombres_copia[j]
                nombres_copia[j] = aux_nombre
                aux1 = p1_copia[i]
                p1_copia[i] = p1_copia[j]
                p1_copia[j] = aux1
                aux2 = p2_copia[i]
                p2_copia[i] = p2_copia[j]
                p2_copia[j] = aux2
                aux3 = p3_copia[i]
                p3_copia[i] = p3_copia[j]
                p3_copia[j] = aux3
            j = j + 1
        i = i + 1
    # Mostrar
    i = 0
    hay = False
    while i < len(nombres_copia):
        if nombres_copia[i] != "":
            hay = True
            print("| NOMBRE PARTICIPANTE: ", nombres_copia[i])
            print("| PUNTAJE JURADO 1: ", p1_copia[i])
            print("| PUNTAJE JURADO 2: ", p2_copia[i])
            print("| PUNTAJE JURADO 3: ", p3_copia[i])
            promedio = calcular_promedio(p1_copia[i], p2_copia[i], p3_copia[i])
            print(f"| PUNTAJE PROMEDIO: {promedio:.2f}/10")
            print()
        i = i + 1
    if not hay:
        print("No hay participantes cargados.") 