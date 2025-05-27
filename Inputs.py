def input_entero(mensaje, minimo=None, maximo=None):
    """
    Solicita al usuario un número entero, validando el rango si se especifica.
    Devuelve el entero ingresado.
    """
    while True:
        valor = input(mensaje)
        try:
            num = int(valor)
            if (minimo is not None and num < minimo) or (maximo is not None and num > maximo):
                print(f"Error: el valor debe estar entre {minimo} y {maximo}.")
            else:
                return num
        except:
            print("Error: debe ingresar un número entero.")

def input_string(mensaje, min_len=1, solo_letras_espacios=False):
    """
    Solicita al usuario un string, validando longitud mínima y si solo debe contener letras y espacios.
    Devuelve el string ingresado.
    """
    while True:
        valor = input(mensaje)
        if len(valor) < min_len:
            print(f"Error: el texto debe tener al menos {min_len} caracteres.")
            continue
        if solo_letras_espacios:
            valido = True
            i = 0
            while i < len(valor):
                c = valor[i]
                if not ((c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') or c == ' '):
                    valido = False
                i = i + 1
            if not valido:
                print("Error: solo se permiten letras y espacios.")
                continue
        return valor

def input_opcion_menu(mensaje, opciones_validas):
    """
    Solicita al usuario una opción del menú, validando que esté en la lista de opciones válidas.
    Devuelve la opción elegida como string.
    """
    while True:
        valor = input(mensaje)
        if valor in opciones_validas:
            return valor
        # Concatenar opciones manualmente
        opciones_str = ""
        i = 0
        while i < len(opciones_validas):
            opciones_str = opciones_str + str(opciones_validas[i])
            if i < len(opciones_validas) - 1:
                opciones_str = opciones_str + ", "
            i = i + 1
        print(f"Opción inválida. Debe elegir una de: {opciones_str}.") 