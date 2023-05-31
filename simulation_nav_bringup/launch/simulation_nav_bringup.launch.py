import os
import subprocess
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory

def generate_launch_description():
    res = []

    # el launcher de el mundo en gazebo
    launch_robot_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("proy_techcommit_mundo"), 'launch/turtlebot3_proy_techcommit.launch.py'))
    )
    res.append(launch_robot_world)

    # el launcher para abrir my_nav2_waypoints_follower.launch
    launch_robot_move = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("proy_techcommit_my_nav2_system"), 'launch/my_nav2_waypoints_follower.launch.py'))
    )
    res.append(launch_robot_move)

    # para abrir la pagina del login de pacobot
    html_file_path = os.path.join(os.path.expanduser('~'),  'ws_ros_web', 'webs','web_pacobot', 'index.html')
    subprocess.Popen(['xdg-open', html_file_path])

    # lo que pondriamos en los terminales para iniciar el server y el rosbridge, ademas de anyadir el inicial pose y cargar el mapa en rviz ademas de lanzar el my_waypoint_follower
    commands = [
        'python3 -m http.server 8000',
        'ros2 launch rosbridge_server rosbridge_websocket_launch.xml',
        'ros2 service call map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_my_nav2_system/config/my_map.yaml}";ros2 service call map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_my_nav2_system/config/my_map.yaml}";ros2 service call map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/turtlebot3_ws/src/proy_techcommit/proy_techcommit_my_nav2_system/config/my_map.yaml}";ros2 run proy_techcommit_my_nav2_system initial_pose_pub; ros2 run proy_techcommit_my_nav2_system my_waypoint_follower'
    ]
    for command in commands:# recorremos la lista lanzando todos los comandos en terminales diferentes
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])


    return LaunchDescription(res)
