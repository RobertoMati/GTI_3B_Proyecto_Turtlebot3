from setuptools import setup
import os
from glob import glob

package_name = 'proy_techcommit_my_nav2_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*.pgm')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'config'), glob('config/*.rviz')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),  
        (os.path.join('share', package_name, 'config'), glob('config/*.lua')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')), 
        (os.path.join('share', package_name, 'config'), glob('config/*.xml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alumno',
    maintainer_email='61469172+quiqueferre12@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'initial_pose_pub = proy_techcommit_my_nav2_system.initial_pose_pub:main', #añadir
            'my_waypoint_follower = proy_techcommit_my_nav2_system.my_waypoint_follower:main', #añadir
        ],
    },
)