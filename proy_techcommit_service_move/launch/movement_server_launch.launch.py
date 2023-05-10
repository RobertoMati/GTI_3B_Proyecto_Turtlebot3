from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='proy_techcommit_service_move',
            executable='movement_server',
            output='screen'
        ),
    ])