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

### Navegación del robot real
Para que funcione correctamente se deben seguir los siguientes pasos:

#Terminal 1 (Conexión con Turtlebot3)
ssh ubuntu@192.168.0.63
password: turtlebot
ros2 launch turtlebot3_bringup robot.launch.py

#Terminal 2
ros2 launch proy_techcommit_my_nav2_system_real my_tb3_sim_nav2_real.launch.py use_sim_time:=False

#Antes de continuar con las terminales, en RViz se deben cambiar los siguientes aspectos:
1. Cambiar el topic general a /map.
2. Eliminar el componente Map y volver a añadirlo.
3. En Map, se debe cambiar un parámetro a Best Effort.
4. Cargar el modelo del robot de su ubicación correspondiente.

#Terminal 3
ros2 service call /map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_provide_map_real/map/src.yaml}"

### En RViz
1. Añadir la pose inicial del robot con 2D estimate pose.

Todo debe verse de color verde, el mapa cargado, el robot cargado y las TF y LaserScan enviando información.

### Probar el funcionamiento
1. Añadir una goal pose para que el robot se mueva hacia su destino.

### Uso de archivo de navegación por puntos my_waypoint_follower
Necesitaremos 3 terminales:
1. En el terminal 1 lanzaremos nuestro mundo: 
ros2 launch proy_techcommit_mundo turtlebot3_proy_techcommit.launch.py
2. En el terminal 2 lanzaremos el launch de my_waypoints que nos abrirá el RVIZ:
ros2 launch proy_techcommit_my_nav2_system my_nav2_waypoints_follower.launch.py
3. En el tercer terminal primero cargaremos el mapa:
ros2 service call map_server/load_map nav2_msgs/srv/LoadMap "{map_url: X/turtlebot3_ws/src/proy_techcommit/proy_techcommit_my_nav2_system/config/my_map.yaml}"
*Sustituir X en map_url: X/turtlebot3_ws por la ruta en la que tengas tu proyecto*
Seguidamente le cargamos la posicion inicial: ros2 run proy_techcommit_my_nav2_system initial_pose_pub
Y para terminar introducimos el siguiente comando en la terminal: ros2 run proy_techcommit_my_nav2_system my_waypoint_follower

### Cámara del robot real en web y movimiento
#Terminal 1 (Conexión con Turtlebot3)
ssh ubuntu@192.168.0.63
password: turtlebot
ros2 launch turtlebot3_bringup robot.launch.py

#Terminal 2 (Encender cámara)
ssh ubuntu@192.168.0.63
ros2 run image_tools cam2image --ros-args -p burger_mode:=false -p frequency:=10.0

#Terminal 3 (Ver cámara por terminal) OPCIONAL
ros2 run image_tools showimage --ros-args -p show_image:=true -p reliability:=best_effort 

#Terminal 4 (Lazar bridge)
ros2 launch rosbridge_server rosbridge_websocket_launch.xml

#Terminal 5 (Lanzar servidor para web)
python3 -m http.server 8000

#Terminal 6 (Video Web Server)
ros2 run web_video_server web_video_server

#Terminal 7 (Servicio para mover el robot)
ros2 launch proy_techcommit_service_move movement_server_launch.launch.py 



