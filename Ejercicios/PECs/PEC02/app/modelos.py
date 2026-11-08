# Defino las variables
tarea = str
tareas = []
tarea_n = []   
terminada = bool
clave = str
globaltarea_n = []   
continuar = True
extra = []
p = True

# creo los import
import re

import os
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Import art
from art import *
autoreset=True

#Import colorama
from colorama import *
#initialization
init(autoreset=True)
from colorama import just_fix_windows_console
just_fix_windows_console()

#dependencias de otros ficheros
from app.operaciones import añade_tarea, buscar_tarea, listar_tareas_pend


def menu():
    """ Lógica del programa, decide qué función ejecutar en cada caso"""
    continuar = True
    while continuar == True:
        main()
        selecc= input("\nElige tu opción: ")
        if selecc == "a":
            añade_tarea()
        elif selecc == "v":
            listar_tareas_pend()   
        elif selecc == "b":
            buscar_tarea()
        elif selecc == "s":
            continuar=False
        else:
            print("\nOpción no válida. Por favor, elige una opción válida.")


def main():
    """ Imprime el menú de opciones a presentar al usuario"""
    clear()
    continuar = True
    print_bienve()
    print(Style.BRIGHT + Back.WHITE + "\n Selecciona una de estas opciones:")
    print(Style.BRIGHT + Back.RED + "a", "---","Añadir tarea")
    print(Style.BRIGHT + Back.RED + "v", "---", "ver lista de tareas pendientes")
    print(Style.BRIGHT + Back.RED + "b", "---", "Buscar una tarea o clave por un texto")
    print(Style.BRIGHT + Back.RED + "s", "---", "Salir del programa")



def print_bienve():
    """"Imprime la cabecera del programa en la UI."""
    art=text2art("TAREAS", font='block', chr_ignore=True)
    print(art)