""" Gestor de Tareas CLI Profesional (Estructura Modular) """

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

#import colorama as col
#import art as art
import os
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

from app.operaciones import añade_tarea, buscar_tarea, listar_tareas_pend, listar_tareas_todas
from app.modelos import tareas


clave = "clave1"
tarea = "tarea1"
terminada = False
extra_tipo1 = "fecha"
extra_texto1 = "2023-10-01"
extra1 = [extra_tipo1, extra_texto1]
extra_tipo2 = "prioridad"
extra_texto2 = "alta"
extra2 = [extra_tipo2, extra_texto2]
extra = [extra1, extra2]
tareas.append([clave, tarea, terminada, extra])
clave = "clave2"
tarea = "tarea2"
terminada = False
extra_tipo1 = "fecha2"
extra_texto1 = "2024-10-01"
extra1 = [extra_tipo1, extra_texto1]
extra_tipo2 = "prioridaddd"
extra_texto2 = "altaddd"
extra2 = [extra_tipo2, extra_texto2]
extra = [extra1, extra2]
tareas.append([clave, tarea, terminada, extra])
clave = "clave3"
tarea = "tarea3"
terminada = True
extra_tipo1 = "fecha3"
extra_texto1 = "2021-10-01"
extra1 = [extra_tipo1, extra_texto1]
extra_tipo3 = "prioridaddd3333"
extra_texto3 = "altadddffff"
extra3 = [extra_tipo3, extra_texto3]
extra = [extra1, extra2, extra3]
tareas.append([clave, tarea, terminada, extra])


continuar = True
def main():
#    clear()
    print("Bienvenido a tu aplicación de control de tareas\n")
    print("Estas son las opciones:\n")
    print("1 Añadir tarea")
    print("a Ver todas las tareas")
    print("p Ver lista de tareas pendientes")
    print("3. Buscar una tarea o clave por texto")
    print("0. Salir del programa")

while continuar == True:
    main()
    selecc= input("\nElige tu opción: ")
    if selecc == "1":
        añade_tarea()
    elif selecc == "p":
        listar_tareas_pend()   
    elif selecc == "a":
        listar_tareas_todas()
    elif selecc == "3":
        buscar_tarea()
    elif selecc == "0":
        continuar=False
    else:
        print("\nOpción no válida. Por favor, elige una opción válida.")