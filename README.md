# Proyecto de Predictor de Saltos para el curso CI-0120 Arquitectura de Computadores de la Universidad de Costa Rica

## Descripción
Este proyecto contiene los predictores de saltos de 2 bits de saturación y global de 2 niveles. Estos predictores seran probados con el benchmark SPECInt2000 del gcc compiler.

- El predictor de salto de 2 bits se compone de una tabla de 2^s entradas , donde se indexa la tabla con los últimos s bits de la dirección del PC.
- El predictor de salto global de 2 niveles indexa una tabla de 2^s entradas mediante el uso de un registro global deslizante de g bits, que hace XOR con los últimos s bits de la dirección del PC.

## Ejecución

### Ejecución Predictor de 2 bits
Para ejecutar el programa con el predictor de 2 bits con [INDEX_SIZE] como la cantidad de bits para indexar la tabla, debe ejecutar la siguiente línea en consola:

* Windows:
```bash
python .\src\main.py -s [INDEX_SIZE] -bp 0
```

* Linux:
```bash
python3 .\src\main.py -s [INDEX_SIZE] -bp 0
```

### Ejecución Predictor Global de 2 Niveles
Para ejecutar el programa con el predictor global de 2 niveles con [INDEX_SIZE] como la cantidad de bits para indexar la tabla y [GLOBAL_HISTORY] como la cantidad de bits del registro deslizante, debe ejecutar la siguiente línea en consola:

* Windows:
```bash
python .\src\main.py -s [INDEX_SIZE] -bp 1 -gh [GLOBAL_HISTORY]
```

* Linux:
```bash
python3 .\src\main.py -s [INDEX_SIZE] -bp 1 -gh [GLOBAL_HISTORY]
```

## Créditos
* Autor: Luis Gómez Sánchez - C03309 - luis.gomez20@ucr.ac.cr