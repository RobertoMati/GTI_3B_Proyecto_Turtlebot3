# provide_map.launch.py
import os

import launch.actions
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='proy_techcommit_modelo_reconocimiento',
            executable='proy_techcommit_modelo_reconocimiento',
            output='screen'
        ),
    ])

