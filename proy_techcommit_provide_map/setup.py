from setuptools import setup
import os #incluir
from glob import glob #incluir

package_name = 'proy_techcommit_provide_map'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'map'), glob('map/*.pgm')),#incluir
        (os.path.join('share', package_name, 'map'), glob('map/*.yaml')),#incluir
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),#incluir
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),#incluir
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
        ],
    },
)
