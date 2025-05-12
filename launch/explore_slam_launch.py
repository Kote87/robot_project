#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

pkg_share = get_package_share_directory('robot_project')
cfg = lambda n: os.path.join(pkg_share, 'config', n)

def generate_launch_description():
    return LaunchDescription([
        # ---- SLAM Toolbox -------------------------------------------
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            parameters=[{'use_sim_time': True}]
        ),
        # ---- Tu nodo de exploración ---------------------------------
        Node(
            package='robot_project',
            executable='exploration_node',
            name='exploration_node',
            parameters=[cfg('exploration.yaml')]
        ),
    ])