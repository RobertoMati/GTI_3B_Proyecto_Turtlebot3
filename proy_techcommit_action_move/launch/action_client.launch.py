from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='proy_techcommit_action_move',
            executable='action_client',
            output='screen'
        ),
    ])