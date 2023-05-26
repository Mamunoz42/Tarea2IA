
## Instalación
Para ejecutar el codigo deben instalar las siguienes librerías:
- pygame


## Ejecución 
Posibles modos de ejecución:

Para jugar Humano-Robot: 
```
python main.py
```

Para ver juego Robot-Robot 
```
python main.py -np
```

Para ejecutar el juego Robot-Robot sin interfaz grafica
```
python main.py -np -nogui
```


## Variables
Al principio del archivo main se encuentran variables que pueden ser modificadas por le alumne:

-noplayer  o -np que automáticamente cambia al jugador humano por un robot.
-nomarbles  o -nm que provoca que no se muestren las canicas en el tablero.
-noscreens  o -ns que provoca que no se muestren las pantallas de inicio y finales del juego. Así no tienen que apretar start o restart para volver a jugar.
-sizeN  donde N es un entero, automáticamente cambia el tamaño del tablero a uno de NxN.
-ngamesN  donde N es un entero, se usa en conjunto con los otros parámetros para simular varios juegos de forma automática.
-write  genera un archivo simulacion.json con los datos de la simulacion.


Ejemplo:
```
python main.py -np -ns -size8 -ngames10 -write
```

