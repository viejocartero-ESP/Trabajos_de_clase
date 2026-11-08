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


def main():
    """ Imprime el menú de opciones a presentar al usuario"""
    clear()
    continuar = True
    print_bienve()
    print("\nSelecciona una de estas opciones:")
    print(Style.BRIGHT + Back.RED + "a", "  ","Añadir tarea")
    print(Style.BRIGHT + Back.RED + "x", "  ", "Ver todaX las tareas")
    print(Style.BRIGHT + Back.RED + "v", "  ", "ver lista de tareas pendientes")
    print(Style.BRIGHT + Back.RED + "b", "  ", "Buscar una tarea o clave por un texto")
    print(Style.BRIGHT + Back.RED + "s", "  ", "Salir del programa")


#Texto Art Form https://patorjk.com/software/taag/#p=testall&f=Slant+Relief&t=Control+de+tareas&x=none&v=4&h=4&w=80&we=false

def print_bienve():
    """"Imprime la cabecera del programa en la UI."""
    print(Style.BRIGHT + Back.WHITE + "BIENVENIDO AL CONTROL DE TAREAS")