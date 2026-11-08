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
from app.modelos import menu


#Lógica del programa
menu()