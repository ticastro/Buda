# Buda

## Lenguaje

- Python (v3.10.1)

## Librerías utilizadas

- Os
- Collections
- Unittest

# Archivos de input

- Para el input de las estaciones a evaluar, se utilizaron archivos con extensión csv. Dentro de estos archivos viene la información de cada una de las estaciones de la red de metro que se quiere, en donde cada línea corresponde a una estación distinta. El formato de los archivos es Identificador_de_estacion,color_de_estacion,vecino1,vecino2,...vecinoN. Cabe destacar que las líneas pueden ser de distintos largos, ya que una estación puede tener una variada cantidad estaciones a las cuales puede llegar. Sin embargo, esto no presenta problemas para la lectura de datos ya que al obtenerlos se trata la línea como una lista, siendo los vecinos la lista "líneas[2:]". 

# Flujo

- Se desarrolló un flujo para utilizar el programa a través de la consola. Para ello, en principio se muestran todos los archivos que se encuentran en la carpeta de test, solicitando que se ingrese un número como input, que está relacionado con un archivo, de manera que en principio el usuario puede seleccionar que archivo desea evaluar. De la misma manera, se solicita la estación inicial y la final, para por útlimo solicitar un color para el tren a evaluar. Así, una vez obtenidos todos los inputs, se entregan las estaciones necesarias para llegar del inicio al final.
- Destacar que si se quiere probar inputs propios, estos se pueden agregar los propios archivos de input a la carpeta test, en donde es necesario que tengan el formato indicado anteriormente. Además, el archivo de input en la carpeta de test corresponde a la información del ejemplo entregado en el enunciado del problema.
- Para correr el programa con el flujo indicado, se debe correr el archivo main.py, perteneciente a la carpeta src/main

# Explicación de algoritmo BFS modificado

- Para encontrar la ruta más corta, se utiliza un algoritmo de BFS modificado para el caso. Lo que se hace es generar un stack como estructura de datos, la cuál permite agregar datos tanto al principio como al final de la lista. Este stack es utilizado como la cola a la cual se le agregan los nodos que se deben recorrer en el BFS. De esta manera, se comienza agregando el nodo de inicio y se recorre como un BFS, hasta que encuentro una estación que, por la lógica de los colores, debería saltarme. Ahí, en vez de agregar el nodo al final de la cola, se agrega al principio, de manera que tenga la misma prioridad del nodo que me salté. Con ello, se genera el efecto de que, al saltar una estación, reviso inmediatamente sus vecinos como si estos estuvieran en la posición de la estación saltada. De esta manera, se encuentra la ruta más corta hacia el nodo final, saltando las estaciones correspondientes.

# Test

- Para testear la aplicación, se genera la carpeta test_src, la cual posee los mismos archivos de src, con 2 archivos de test agregados. De esta manera, se generan test solamente para las clases, en donde se ve que estas sean bien creadas, y que se utilicen bien las funciones dentro de ellas. Para correr los test de la clase station, es necesario correr el archivo test_src/main/classes/test_station.py, mientras que para correr los test de la clase subwayNetwork, es necesario correr el archivo test_src/main/classes/test_subwayNetwork.py.

