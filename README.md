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
    |__ *Más paquetes que puedan haber*
```

## Pasos para montar el proyecto correctamente
Para el correcto funcionamiento del proyecto, se deben seguir los siguientes pasos a la hora de hacer un **colcon build**:
- 0: Abrir una **Terminal**
- 1: Situarse en turtlebot3_ws con: **cd turtlebot3_ws/**
- 2: Realizar un **colcon build** de turtlebot3_gazebo con: **colcon build --packages-select turtlebot3_gazebo**
- 3: Realizar un **colcon build** global.
- 4: No siempre es necesario, pero por si acaso escribir un **source install/setup.bash** en la terminal.
- 5: Lanzar el fichero de lanzamiento. Para el caso del fichero del mundo, se haría: **ros2 launch proy_techcommit_mundo turtlebot3_proy_techcommit.launch.py**
