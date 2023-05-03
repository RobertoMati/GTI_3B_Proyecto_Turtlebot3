from setuptools import setup
import os
from glob import glob

package_name = 'proy_techcommit_action_move'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robertomati',
    maintainer_email='robertomatillaaugustinus@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_server = proy_techcommit_action_move.action_server:main',
            'action_client = proy_techcommit_action_move.action_client:main',
        ],
    },
)
