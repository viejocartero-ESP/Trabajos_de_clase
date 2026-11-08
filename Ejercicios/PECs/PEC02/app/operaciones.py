from app.modelos import tareas, continuar, main, tarea, clave, tarea_n, extra, p, terminada, clear, re

#terminada = False
def añade_tarea():
    """ Añade tareas. Crea tupla con clave, tarea, terminada. Crea otra tupla con el texto extra,
    n veces la tupla extra_tipo, extra_texto y append esta tupla a la inicial"""
    clave = input("Introduce una clave de la tarea: ")
    tarea = input("Introduce la tarea: ")
    terminada = bool((int(input("Escribe 1 si está terminada, 0 si está pendiente: "))) > 0)     
    mas = input("¿quieres añadir alguna información adicional a la tarea? (s/n): ")
    extra = []
    while mas == "s":
        extra_tipo = input("Escribe el tipo de información extra que quieres añadir: ")
        extra_texto = input("Escribe el texto de la información extra: ")
        extra += [extra_tipo, extra_texto]
        mas = input("¿quieres añadir  información extra a la tarea? (s/n): ")
    tarea_n = [clave, tarea, terminada, extra]
    tareas.append(tarea_n)


def listar_tareas_todas():
    """ Imprime todas las tareas. Bucle for que recorre la tupla tareas, pasa a txt el contenido de cada elemento, 
    le quita caracteres molestos y lo imprime"""
    print("\nTodas las tareas:\n")
    for i in range(len(tareas)):
            text = str(f"Clave: {tareas[i][0]}, Tarea: {tareas[i][1]}, terminada: {tareas[i][2]}, {tareas[i][3]}")
            text = re.sub(r"[\[\]']", "", text)
            print(text)
    input("Presiona Enter para continuar...")

def listar_tareas_pend():
    """ Imprime las tareas pendientes. Recorre cada elemento de la tupla tareas y cuando está 
    pendiente (tercer campo, tareas[i][2]) pasa a txt su contenido, le quita caracteres molestos y lo imprime"""
    print("\nTareas pendientes:\n")
    for i in range(len(tareas)):
        if tareas[i][2] == False:
            text = str(f"Clave: {tareas[i][0]}, Tarea: {tareas[i][1]}, terminada: {tareas[i][2]}, {tareas[i][3]}")
            text = re.sub(r"[\[\]']", "", text)
            print(text)
    input("Presiona Enter para continuar...")

def buscar_tarea():
    """ Busca las tareas que incluyen, en cualquier lugar, el texto seleccionado. Recorre la tupla tareas, pasa a 
    txt cada elemento, busca el texto seleccionado, si lo encuentra imprime su contenido quitándole caracteres molestos"""
    found = False
    clave_buscar = input("Introduce texto a buscar: ")
    for i in range(len(tareas)):
        text = str(f"Clave: {tareas[i][0]}, Tarea: {tareas[i][1]}, terminada: {tareas[i][2]}, {tareas[i][3]}")
        if clave_buscar in text:
            print(re.sub(r"[\[\]']", "", text))
            found = True
    if not found:
        print("No se encontró ninguna tarea con ese texto.")
    input("\nPresiona Enter para continuar...")