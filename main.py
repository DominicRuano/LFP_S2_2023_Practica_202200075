import os
import tkinter as tk
from tkinter import filedialog 

#Funciones
def default():
    print("Opcion no valida")

def get_inf():
    print("Creando informe...")

def get_mov():
    print("get mov")

def get_inv():
    print("obteniento inventario:")
    path_inv = get_path()
    archivo = open(path_inv, "r")
    
    linea = archivo.readline().strip()
    while linea:
        if "crear_producto" in linea:
            temp = linea.split(" ")
            temp2 = temp[1].split(";")
            lista.append(temp2)
        
        linea = archivo.readline().strip()
    print(lista)

def get_path():
    path = filedialog.askopenfile(title="Select file",filetypes=(("inv files", ".inv"),("all files", ".*")))
    print("El path es: {}".format(path.name))
    if input("¿Esta seguro que ese es el archivo correcto? (s/n): ").lower() == "s":
        return path.name
    else:
        return get_path()

def main():
    print("+ ", len(titulo)*"-", " +", sep="")
    print("|", titulo, "|")
    print("+ ", len(titulo)*"-", " +", sep="")

    print("\n# Sistema de inventario:\n")
    print("1. Carga de inventario inicial")
    print("2. Carga de instrucciones de movimientos")
    print("3. Crear informe de inventario")
    print("4. Salir\n")

    if path_inv != None:
        print("Se agrego un inventario inicial.")

    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        get_inv()
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    else:
        pass

#Variables
titulo = "practica 1 - lenguajes formales de programacion"
path_inv = None
lista = [] # lsita de listas sintaxis: [[],[],[nombre, cantidad, precio, bodega]]
#Nombre = []

#Main
if __name__ == "__main__":
    os.system("cls")
    while True:
        main()
