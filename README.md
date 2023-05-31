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

## Navegación del robot real
Para que funcione correctamente se deben seguir los siguientes pasos:

#### Terminal 1 (Conexión con Turtlebot3)
```
ssh ubuntu@192.168.0.63
```
##### Terminal 1 - password: 
```
turtlebot
```
```
ros2 launch turtlebot3_bringup robot.launch.py
```

#### Terminal 2
```
ros2 launch proy_techcommit_my_nav2_system_real my_tb3_sim_nav2_real.launch.py use_sim_time:=False
```

##### Antes de continuar con las terminales, en RViz se deben cambiar los siguientes aspectos:
1. Cambiar el topic general a /map.
2. Eliminar el componente Map y volver a añadirlo.
3. En Map, se debe cambiar un parámetro a Best Effort.
4. Cargar el modelo del robot de su ubicación correspondiente.

#### Terminal 3
```
ros2 service call /map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_provide_map_real/map/src.yaml}"
```

#### En RViz
1. Añadir la pose inicial del robot con 2D estimate pose.
2. Todo debe verse de color verde, el mapa cargado, el robot cargado y las TF y LaserScan enviando información.

#### Probar el funcionamiento
1. Añadir una goal pose para que el robot se mueva hacia su destino.





## Uso de archivo de navegación por puntos my_waypoint_follower
Necesitaremos 3 terminales:
#### Terminal 1 (lanzaremos nuestro mundo): 
```
ros2 launch proy_techcommit_mundo turtlebot3_proy_techcommit.launch.py
```

#### Terminal 2 (lanzaremos el launch de my_waypoints que nos abrirá el RVIZ):
```
ros2 launch proy_techcommit_my_nav2_system my_nav2_waypoints_follower.launch.py
```
#### Terminal 3 (cargaremos el mapa):
```
ros2 service call map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_my_nav2_system/config/my_map.yaml}"
```

#### Terminal 3 (Seguidamente le cargamos la posicion inicial):
```
ros2 run proy_techcommit_my_nav2_system initial_pose_pub
```

#### Terminal 3 (llamamos a waypoint_follower): 
```
ros2 run proy_techcommit_my_nav2_system my_waypoint_follower
```




## Funcionamiento completo (conexión con Pacobot - web - waypoints - real y simulación)
#### Terminal 1 (Conexión con Turtlebot3)
```
ssh ubuntu@192.168.0.63
```

##### Terminal 1 - password: 
```
turtlebot
```
```
ros2 launch turtlebot3_bringup robot.launch.py
```

#### Terminal 2 (Encender cámara)
```
ssh ubuntu@192.168.0.63
```

```
ros2 run image_tools cam2image --ros-args -p burger_mode:=false -p frequency:=10.0
```

#### Terminal 3 (Ver cámara por terminal) OPCIONAL
```
ros2 run image_tools showimage --ros-args -p show_image:=true -p reliability:=best_effort 
```

#### Terminal 4 (Lazar bridge)
```
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```

#### Terminal 5 (Lanzar servidor para web)
```
python3 -m http.server 8000
```

#### Terminal 6 (Video Web Server)
```
ros2 run web_video_server web_video_server
```

#### Terminal 7 (Servicio para mover el robot)
```
ros2 launch proy_techcommit_service_move movement_server_launch.launch.py 
```

#### Terminal 8 (Lanzamiento modelo reconocimiento; Desde proy_techcommit/proy_techcommit_modelo_reconocimiento/proy_techcommit_modelo_reconocimiento)
```
python3 proy_techcommit_modelo_reconocimiento.py 
```

##### A partir de esta terminal son lanzamientos para simulación

#### Terminal 9 (Lanzar mundo simulación)
```
ros2 launch proy_techcommit_mundo turtlebot3_proy_techcommit.launch.py
```

#### Terminal 10 (launch de my_waypoints que nos abrirá el RVIZ)
```
ros2 launch proy_techcommit_my_nav2_system my_nav2_waypoints_follower.launch.py
```
##### Pasos a seguir antes de continuar con la siguiente terminal:
1. Cargar el modelo del robot correctamente

#### Terminal 11 (Cargar el mapa)
```
ros2 service call map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_my_nav2_system/config/my_map.yaml}"
```
##### Después:
```
ros2 run proy_techcommit_my_nav2_system initial_pose_pub
```
##### Finalmente:
```
ros2 run proy_techcommit_my_nav2_system my_waypoint_follower
```

## Launch de lanzadores y de comandos de la navegación del robot por puntos vía web
#### Pasos a seguir para lanzar el entorno y cargar la web
0. Nos colocamos dentro de la carpeta turtlebot3_ws y hacemos colcon de la carpeta del proyecto (este paso es opcional Terminal 1)
```
colcon build --packages-select proy_techcommit
```
1. Lanzamos el launch del paquete simulation_nav_bringup(Terminal 1):
```
ros2 launch simulation_nav_bringup simulation_nav_bringup.launch.py
```
2. Observar que tiene los siguientes elementos: 
 - El mapa del entorno virtual en Gazebo
 - El Rviz con el mapa escaneado cargado y el initial pose ejecutado además del servicio de my_waypoint_follower activado, todo esto se podrá ver en un mismo terminal como en el siguiente ejemplo (Terminal 2 *Se abre sola*): 
```
...
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), result=0)
[INFO] [1685532088.673902522] [initial_pose_pub_node]: Hola Publishing Initial Position  
 X= 0.2 
 Y=0.0 
 W = 1.0 
```
 - La pantalla login.htm también deberá verse abierta dentro de alguno de los navegadores web.
 - Un http.server ejecutado en el puerto 8000, en alguna de las 4 terminales que hay abiertas, se tiene que ver algo así (Terminal 3 *Se abre sola*):
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```
 - En otro terminal distinto, el rosbridge_server, se tiene que observar algo similar a este ejemplo(Terminal 4 *Se abre sola*):
 
```
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [rosbridge_websocket-1]: process started with pid [2670]
[INFO] [rosapi_node-2]: process started with pid [2672]
[rosbridge_websocket-1] [INFO] [1685532078.666935906] [rosbridge_websocket]: Rosbridge WebSocket server started on port 9090
```
#### Posibles errores o problemas al lanzar el entorno y carga de la web
- En Rviz no me carga el modelo del robot: Busca en tu directorio el modelo turtlebot3_burguer/ _pi que contenga .urdf
- No se abre el archivo .html: Dentro del paquete simulation_nav_bringup en la carpeta launch, encontramos el archivo: simulation_nav_bringup.launch.py, en la línea 24 del código encontramos la ruta donde viene predefinida mi archivo web, en mi caso: 
```
html_file_path = os.path.join(os.path.expanduser('~'), 'turtlebot3_ws', 'ws_ros_web', 'web_pacobot', 'login.html')
```
Cambia los espacios entre comillas, añadiendo, quitando o modificando su contenido hasta ubicar correctamente su ruta.
Tras eso, guarda los cambios y de nuevo sitúate en la carpeta turtlebot3_ws y hacemos colcon del paquete en cuestión para actualizar los cambios.
```
colcon build --packages-select simulation_nav_bringup
```
Una vez haya finalizado, cierras todos los terminales y ventanas que tengas abiertas en relación con el launch y ejecutamos:
```
ros2 launch simulation_nav_bringup simulation_nav_bringup.launch.py
```
Si surgen nuevos problemas o errores, no dudéis en poneros en contacto con los miembros del equipo



