# BIBLIOTECAS

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import pickle

# FUNCIONES

def limpiar_consola():
    if os.name == 'posix':
        _ = os.system('clear')  # Para Unix/Linux (incluyendo Mac)
    else:
        _ = os.system('cls')    # Para sistemas Windows

def validacion(opciones, opcion):
    palabra = ""
    for i in range(0, len(opciones)):
        palabra = palabra + " " + opciones[i]
    estado = False
    for i in range(0, len(opciones)):
        if opciones[i] == opcion:
            estado = True
    while estado == False:
        print(f"Opción incorrecta, solo puedes elegir entre: {palabra}")
        opcion = input("Inténtalo de nuevo: ")
        for i in range(0, len(opciones)):
            if opciones[i] == opcion:
                estado = True
    return opcion

def bienvenida():
    print()
    print("Bienvenido al asistente de análisis y visualización de datos")
    print()
    print("Descripción")
    print("El programa está diseñado para ayudar al usuario a visualizar gráficos de datos, ver datos estadísticos, crear gráficos personalizados y datos para un análisis posterior, y más.")
    print()
    print("Si deseas colaborar con el proyecto, el repositorio es el siguiente: https://github.com/mastercodemachine/Ia_asis.git")
    print()
    print("Si deseas donar para apoyar el proyecto, la CBU es la siguiente:")
    print()
    input("Presiona cualquier tecla para continuar: ")

def menu1():
    limpiar_consola()
    print()
    print("---------------- MENÚ ----------------")
    print()
    print("1 - Crear un archivo de trabajo")
    print("2 - Seleccionar un archivo de trabajo")
    print("3 - Cargar una base de datos")
    print("4 - Salir")
    print()
    opcion_menu1 = input("¿Qué te gustaría hacer? (elige 1 o 2 o 3 o 4): ")
    opcion_menu1 = validacion(["1","2","3", "4"], opcion_menu1)
    return opcion_menu1

def carga_de_datos():
    opcion = input("¿Quieres crear datos o cargar un conjunto de datos existente? CREAR/CARGAR: ")
    opcion = validacion(["CREAR","CARGAR"], opcion)

def vincular_basededatos():
    print()
    pregunta = input("¿Deseas vincular el archivo con una base de datos ahora? (SI/NO): ").upper()
    pregunta = validacion(["SI","NO"], pregunta)
    if pregunta == "SI":
        pass
    else:
        pregunta = input("¿Deseas crear otro archivo? (SI/NO): ").upper()
        pregunta = validacion(["SI","NO"], pregunta)
        if pregunta == "SI":
            create()
        else:
            pass

def crear():
    nombre = input("Ingresa un nombre para el archivo: ")
    nombre = ArchivoDeDatos()
    nombre.nombre = str(nombre)
    vincular_basededatos()

# CLASES

class ArchivoDeDatos:
    data = 'default'
    def __init__(self, nombre, data):
        self.nombre = nombre
        self.data = data

# INICIALIZACIÓN DE VARIABLES

registro_archivos = "registro.pkl"
registro_BasesDatos = "base_de_datos.pkl"

# INICIO DEL PROGRAMA

inicio = 1

while inicio == 1:
    bienvenida()
    opcion_menu1 = menu1()

    if opcion_menu1 == "1":
        crear()
    elif opcion_menu1 == "2":
        pass
    elif opcion_menu1 == "3":
        pass 
    else:
        inicio = 0
        print()
        input("Adiós")
