from setuptools import setup
import os
from glob import glob

package_name = 'proy_techcommit_modelo_reconocimiento'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'proy_techcommit_modelo_reconocimiento = proy_techcommit_modelo_reconocimiento.proy_techcommit_modelo_reconocimiento:main'
        ],
    },
)
