# GTI 3B Proyecto Turtlebot3
## Importar correctamente el proyecto
Deberemos colocar este repositorio dentro de **turtlebot3_ws/src**, y la carpeta inicial debe llamarse **proy_techcommit**.
Para comprobar que se ha añadido y editado correctamente, la distribución debería quedar de la siguiente manera:
```
turtlebot3_ws
|
|__ build **(si no se ha realizado ningún colcon build esta carpeta aún no existe)**
|__ install **(si no se ha realizado ningún colcon build esta carpeta aún no existe)**
|__ log **(si no se ha realizado ningún colcon build esta carpeta aún no existe)**
|__ src
    |__ turtlebot3_simulations
    |__ turtlebot3_gazebo
    |__ turtlebot3_fake_node
    |__ proy_techcommit
        |__ proy_techcommit
        |__ proy_techcommit_mundo
        |__ *Más paquetes*
    |__ *Más paquetes que puedan haber*
```

## Pasos para montar el proyecto correctamente la primera vez
### Cambios de lineas de archivos

Antes de realizar el montaje del proyecto, se deben cambiar y/o añadir, comentando las existentes, dos líneas existentes en el fichero CMakeLists.txt de **proy_techcommit_mundo**, cambiando la ruta por la propia del usuario.

```
#set(CMAKE_PREFIX_PATH "ruta del usuario a turtlebot3_ws/install/turtlebot3_gazebo" ${CMAKE_PREFIX_PATH}) 
list(APPEND CMAKE_PREFIX_PATH "ruta del usuario a turtlebot3_ws/install/turtlebot3_gazebo")
```
### Añadir carpetas (en el caso de que no se hayan incluido)
En el espacio de trabajo hay carpetas vacias, y como en GitHub no se pueden incluir este tipo de carpetas, directamente no las incluye. Por eso, debe revisarse una vez importado el proyecto que **proy_techcommit** quede exactamente de la siguiente manera:
```
|__ proy_techcommit
|        |__ proy_techcommit
|            |__ CMakeLists.txt
|            |__ package.xml
|        |__ proy_techcommit_mundo
|        |   |__ CMakeLists.txt
|        |   |__ package.xml
|        |   |__ docs
|        |   |__ launch
|        |   |__ include *Esta sería la carpeta a añadir, porque dentro solo tiene una carpeta vacía*
|        |       |__ proy_techcommit *Esta subcarpeta también debe añadirse si no estaba la anterior*
|        |   |__ models
|        |   |__ photos
|        |   |__ src
|        |   |__ urfd
|        |   |__ world
|        |___________________
|__________________________________
```

### Montar el proyecto (sirve para la primera vez y futuras)
Para el correcto funcionamiento del proyecto, se deben seguir los siguientes pasos a la hora de hacer un **colcon build**:
- 0: Abrir una **Terminal**
- 1: Situarse en turtlebot3_ws con: **cd turtlebot3_ws/**
- 2: Realizar un **colcon build** de turtlebot3_gazebo con: **colcon build --packages-select turtlebot3_gazebo**
- 3: Realizar un **colcon build** global.
- 4: No siempre es necesario, pero por si acaso escribir un **source install/setup.bash** en la terminal.
- 5: Lanzar el fichero de lanzamiento. Para el caso del fichero del mundo, se haría: **ros2 launch proy_techcommit_mundo turtlebot3_proy_techcommit.launch.py**
