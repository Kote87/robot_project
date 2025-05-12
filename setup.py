from setuptools import setup, find_packages
from glob import glob

package_name = 'robot_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
        ('share/' + package_name + '/config', glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vboxuser',
    maintainer_email='vboxuser@todo.todo',
    description='Nodos de integración para cámara, LIDAR y movimiento del ROSbot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node = robot_project.camera_node:main',
            'movement_node = robot_project.movement_node:main',
            'sensor_listener = robot_project.sensor_listener:main',
            'exploration_node=robot_project.exploration_node:main',
        ],
    },
)
