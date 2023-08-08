import os
import tkinter as tk
from tkinter import filedialog 

#Funciones
def default():
    print("Opcion no valida")

def get_inf():
    print("Creando informe...")
    archivo = open("informe.txt", "w")
    archivo.write("Informe de inventario: ")
    archivo.write("\n\n\n")
    archivo.write("Producto        Cantidad        Precion Unitario        Valor Total        Ubicacion\n")
    archivo.write("---------------------------------------------------------------------------------------\n")

    for a in lista:
        archivo.write(a[0])
        archivo.write((16 - len(a[0])) * " ")
        archivo.write(a[1])
        archivo.write((16 - len(a[1])) * " ")
        archivo.write(a[2])
        archivo.write((24 - len(a[2])) * " ")
        archivo.write(str(float(a[1]) * float(a[2]))) # :))))
        archivo.write((18 - len(str(float(a[1]) - float(a[2])))) * " ")
        archivo.write(a[3])
        archivo.write((19 - len(a[3])) * " ")
        archivo.write("\n")


def get_mov():
    print("obteniento movimientos:")
    path_mov = get_path()
    archivo = open(path_mov, "r")
    
    linea = archivo.readline().strip()
    while linea:
        if "agregar_stock" in linea:
            temp = linea.split(" ")
            temp2 = temp[1].split(";")
            lista_mov.append(temp2)
        elif "vender_producto" in linea:
            temp = linea.split(" ")
            temp2 = temp[1].split(";")
            lista_mov2.append(temp2)
        linea = archivo.readline().strip()

    for a in lista:
        for b in lista_mov:
            if a[0] == b[0]:
                if a[3] == b[2]:
                    a[1] = float(a[1]) + float(b[1])
                else:
                    print("Error: el producto no existe en esa ubicacion.")
        for b in lista_mov2:
            if a[0] == b[0]:
                if a[3] == b[2]:
                    if float(a[1]) >= float(b[1]):
                        a[1] = float(a[1]) - float(b[1])
                    else:
                        print("Error: El producto existente es menos a la cantidad que se desea vender.")
                else:
                    print("Error: el producto no existe en esa ubicacion.")

    print(lista)
    archivo.close()

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
    #print(lista)
    archivo.close()

def get_path():
    path = filedialog.askopenfile(title="Select file",filetypes=(("inv files", ".inv"),("mov files", "mov"),("all files", ".*")))
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
        get_mov()
    elif opcion == 3:
        get_inf()
    elif opcion == 4:
        pass
    else:
        print("Ingrese una opcion valida.")

#Variables
titulo = "practica 1 - lenguajes formales de programacion"
path_inv = None
lista = [] # lista de listas sintaxis: [[],[],[nombre, cantidad, precio, bodega]]
lista_mov = [] # lista de listas sintaxis: [[],[],[nombre, cantidad, bodega]]
lista_mov2 = [] # misma sintaxis que la anterior

#Main
if __name__ == "__main__":
    os.system("cls")
    while True:
        main()
