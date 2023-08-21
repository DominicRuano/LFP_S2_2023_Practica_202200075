# LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION Sección B- 🖥️
## Práctica 1 📚
### SEGUNDO SEMESTRE 2023 📅

```js
Universidad San Carlos de Guatemala 🎓
Programador: Dominic Juan pablo Ruano Perez 🧑‍💻
Carne: 202200075 🆔
```
---
## Descripción del Proyecto📋
Se solicita al estudiante del curso de lenguajes formales y de programación el desarrollo de un programa en Python que permita gestionar un inventario y registrar movimientos de registrar los movimientos de productos utilizando archivos de texto. 📦

se realizo un sistema para la gestion de inventario, generado en base a un archivo con extencion **.inv**, con el anventario generado se pueden hacer movimiento de **agregar stock, venta de productos** los cuales modificaran el inventario inicial.  📈

se genera apartir de los archivos **.inv, .mov** un archivo **.txt** el cual contiene un informe del estado actual del inventaio, constando con las siguiente columnas. 📄

| Producto | Cantidad | Precio unitario | Valor total | Ubicacion |
| --       | --       | --              |  --         | --        |
| Precio del producto  | existencias en inventario | Precio C/U | Precio Total en inventario | Bodega en la que se encuentra |

> Sintaxis de las lista
    *   las listas son llenadas con la siguiente sintaxis, la cual se utilizo para poder tener una mejor accesibilidad de cada atributo.
<img src="https://i.ibb.co/vYvVdRm/code1.png" alt="funcion main" style="width:500px;"/>

## Objetivos 🎯
* Objetivo General
    * Desarrollar un sistema de gestión de inventario en Python que permita la lectura de archivos en formato .inv y .mov para realizar movimientos en el inventario. El sistema deberá implementar los paradigmas de programación vistos en clase y laboratorio. El estudiante deberá diseñar y crear una interfaz de usuario que permita cargar los archivos de inventario y movimientos, procesar los movimientos en el inventario base y generar un archivo de salida en formato .txt con el inventario actualizado.
* Objetivos Específicos
    * El proyecto requerirá que el estudiante desarrolle habilidades sólidas en la manipulación de archivos en Python. Esto incluye la lectura de archivos .inv y .mov, la extracción de datos relevantes y la escritura de los resultados en un archivo de salida .txt.
    * El estudiante deberá aplicar principios de lógica de programación para procesar los movimientos en el inventario. Esto implicará el uso adecuado de estructuras de datos como listas, diccionarios u otras estructuras pertinentes para mantener y actualizar el inventario de manera eficiente.
---


## Herramientas Principales a Utilizar 🛠️
* Visual Studio Code (última versión) 💻
* Python 🐍
* Bibliotecas de Python
    * tkinter 🖼️
    * os 📂
* Git  📜
---

## Enlaces de Utilidad  🔗
*  [instalacion de Python y VSC](https://www.youtube.com/watch?v=bZjulmpBIGk) 📹

___
## Funciones dentro del codigo

>*   Funcion Main()
    esta funcion se encarga de imprimir el menu, y decidir si se decea agregar un inventario, movimientos entre otros.
<img src="https://i.ibb.co/FKMV3zd/code.png" alt="funcion main" style="width:500px;"/>

---

>*   Funcion get_path()
    se encarga de obtener el path del archivo que deseamos leer, tanto del archivo .inv como el .mov
<img src="https://i.ibb.co/KhywGk7/code2.png" alt="funcion main" style="width:500px;"/>

---

>*   Funcion Default()
    Funcion encargada unicamente para reanudad el bucle y regresar al menu en caso que se ingrese un valor no permitido o fuera de rango.
<img src="https://i.ibb.co/4Z36BJL/code6.png" alt="funcion main" style="width:600px;"/>

---

>*   Funcion Get_info()
    Encargada de generar el archivo de reporte.txt
<img src="https://i.ibb.co/S73dTHz/code5.png" alt="funcion main" style="width:500px;"/>

---

>*   Funcion inv()
    Funcion principal del sistema donde se hace lectura del archivo .inv y se crea un inventario en la memoria temporal.
<img src="https://i.ibb.co/Jyg8yy9/code3.png" alt="funcion main" style="width:500px;"/>

---

>*   Funcion mov()
    Es la funcionalidad del sistema donde se hace la lectura del archivo .mov y consecutivamente se realizan los cambios a el inventario anteriormente creado.
<img src="https://i.ibb.co/dP2nVQc/code4.png" alt="funcion main" style="width:500px;"/>

---

>*   Muchas gracias eso seria todo
    gracias por leer todo este documento tenga un buen dia aux.
<img src="https://i.ibb.co/nB08qk2/1ac04daf-e3d7-4dbd-8c43-8877808ec602.jpg" alt="funcion main" style="width:100px;"/>