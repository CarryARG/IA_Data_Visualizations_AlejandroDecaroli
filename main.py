# LIBRERIAS

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# FUNCIONES

def limpiar_consola():
    if os.name == 'posix':
        _ = os.system('clear')  # Para sistemas tipo Unix/Linux (Mac incluido)
    else:
        _ = os.system('cls')    # Para sistemas Windows


def validacion(b,n):
    palabra = ""
    for i in range(0,len(b)):
        palabra = palabra + " " + b[i]
    estado = False
    for i in range(0,len(b)):
        if b[i] == n:
            estado = True
    while estado == False:
        print(f"Opción incorrecta, solo puede elegir entre: {palabra}")
        n = input("Intente de nuevo: ")
        for i in range(0,len(b)):
            if b[i] == n:
                estado = True
    return n


def welcome():
    print()
    print("Bienvenido al asistente de análisis y visualización de datos")
    print()
    print("Descripción")
    print("El programa esta diseñado para ayudar al usuario a visualizar gráficos de datos,\nver datos estadisticos, crear gráficos y datos personalizados para posterior análisis y más.")
    print()
    print("Si quiere colaborar con el proyecto el repositorio del mismo es el siguiente: https://github.com/mastercodemachine/Ia_asis.git")
    print()
    print("Si quiere donar para ayudar con el proyecto, el CBU es el siguiente: ")
    print()
    input("Aprete cualquier tecla para continuar: ")


def menu1():
    limpiar_consola()
    print()
    print("---------------- MENU ----------------")
    print()
    print("1 - Crear archivo de trabajo")
    print("2 - Seleccionar archivo de trabajo")
    print("3 - Salir")
    print()
    opcion_menu1 = input("¿Qué quiere hacer? (elija 1 o 2 o 3): ")
    opcion_menu1 = validacion(["1","2","3"], opcion_menu1)

    return opcion_menu1


def cargadatos():
    opcion = input("¿Quiere crear los datos, o cargar un base existente? CREAR/CARGAR: ")
    opcion = validacion(["CREAR","CARGAR"], opcion)


def crear():
    nombre = input("Ingrese un nombre para el archivo: ")
    cargadatos()
    

# CLASES

class archivo:
    def __init__(self,nombre,bba):
        self.nombre = nombre
        self.bba = bba

# INICIO DEL PROGRAMA

inicio = 1

while inicio == 1:
    welcome()
    opcion_menu1 = menu1()

    if opcion_menu1 == "1":
        crear()
    elif opcion_menu1 == "2":
        pass
    else:
        inicio = 0
        input("Adios")



