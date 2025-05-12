from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

pkg_share = get_package_share_directory('robot_project')
cfg = lambda name: os.path.join(pkg_share, 'config', name)

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_project',
            executable='camera_node',
            name='camera_node',
            parameters=[cfg('camera.yaml')]
        ),
        Node(
            package='robot_project',
            executable='movement_node',
            name='movement_node',
            parameters=[cfg('movement.yaml')]
        ),
        Node(
            package='robot_project',
            executable='sensor_listener',
            name='sensor_listener',
            parameters=[cfg('sensors.yaml')]
        ),
    ])

