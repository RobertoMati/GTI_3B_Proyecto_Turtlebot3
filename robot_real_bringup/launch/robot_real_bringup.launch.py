import os
import subprocess
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory

def generate_launch_description():
    res = []

    # para abrir la pagina del login de pacobot
    html_file_path = os.path.join(os.path.expanduser('~'), 'turtlebot3_ws', 'ws_ros_web', 'web_pacobot', 'index.html')
    subprocess.Popen(['xdg-open', html_file_path])

    

    commandos=[
        'ros2 launch turtlebot3_bringup robot.launch.py',
        'ros2 service call /map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_provide_map_real/map/src.yaml}";ros2 service call /map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_provide_map_real/map/src.yaml}";ros2 service call /map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_provide_map_real/map/src.yaml}"',
        'ros2 launch proy_techcommit_my_nav2_system_real my_nav2__waypoints_follower_real.launch.py use_sim_time:=False'
    ]
    for commandito in commandos:# recorremos la lista lanzando todos los comandos en terminales diferentes
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', commandito])

    commandcam = [
        'ros2 launch proy_techcommit_modelo_reconocimiento modelo_reconocimiento.launch.py'
        
    ]
    
    for commandc in commandcam:# recorremos la lista lanzando todos los comandos en terminales diferentes
        subprocess.Popen(['gnome-terminal', '--disable-factory', '--', 'bash', '-c', commandc])

    comandweb=[
        'ros2 launch rosbridge_server rosbridge_websocket_launch.xml',
        'python3 -m http.server 8000',
        'ros2 run web_video_server web_video_server',
        'ros2 launch proy_techcommit_service_move movement_server_launch.launch.py ',#lanzamos el movimiento del robot
        'python3 proy_techcommit_modelo_reconocimiento.py ',#lanzamos el modelo de reconocimiento
        'ros2 run proy_techcommit_my_nav2_system_real my_waypoint_follower_real',#lanzamos la naegacion por waypoints
        
    ]
    for commandw in comandweb:# recorremos la lista lanzando todos los comandos en terminales diferentes
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', commandw])
    ruta=[
        'cd ',
        'cd /home/alumno/turtlebot3_ws/src/proy_techcommit/proy_techcommit_speech/robot_gandia_speech/robot_gandia_speech',
        'python3 Gandia_Speech.py'
    ]
    #abre el speach para hablar al robot
    for speachc in ruta:
        subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash -c "{}"'.format(speachc)], shell=True)

    return LaunchDescription(res)
