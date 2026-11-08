""" PEC02 Gestor de Tareas CLI Profesional     Jesús Esteban"""

""" Pseudocódigo:
Inicializa diccionario   tareas = {"tarea": tarea, "estado": estado, "palabra clave": clave, "fecha": fecha, "texto_libre": texto}
    Print("Bienvenido a tu aplicación de control de tareas Elige una opción:")
    print("Estas son las opciones:")
    print("1. Añadir tarea")
    print("2. Ver lista de tareas pendientes")
    print("3. Salir del programa")
        if opcion == "1":
            tarea = input("Introduce la tarea: ")
            estado = input("Introduce el estado de la tarea: ")
            clave = input("Introduce la palabra clave de la tarea: ")
            fecha = input("Introduce la fecha de la tarea: ")
            texto = input("Introduce un texto libre para la tarea: ")
            añadir_tarea
        elif opcion == "2":
        listar_tareas()
        elif opcion == "3":
            break

Funciones:    
Modelos: modelo  de datos    
    Inicializa diccionario   tareas = {"tarea": tarea, "estado": estado, "palabra clave": clave, "fecha": fecha, "texto_libre"
operaciones: operaciones sobre los datos
    añadir_tarea(tarea, estado, clave, fecha, texto)
        tareas.append(tarea)
        print("Tarea añadida correctamente.")
    listar_tareas()
        print("Tareas registradas:")
        for i in tareas:
        print( tarea, estado, clave, fecha, texto)
"""

# Importa funciones y variable
from app.operaciones import añade_tarea, buscar_tarea, listar_tareas_pend, listar_tareas_todas
from app.modelos import tareas, continuar, main

#Lógica del programa
while continuar == True:
    main()
    selecc= input("\nElige tu opción: ")
    if selecc == "a":
        añade_tarea()
    elif selecc == "v":
        listar_tareas_pend()   
    elif selecc == "x":
        listar_tareas_todas()
    elif selecc == "b":
        buscar_tarea()
    elif selecc == "s":
        continuar=False
    else:
        print("\nOpción no válida. Por favor, elige una opción válida.")