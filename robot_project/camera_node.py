#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        topic = self.declare_parameter('topic', '/camera/image_raw').value
        self.create_subscription(Image, topic, self.listener, 10)

    def listener(self, msg):
        self.get_logger().info(f'Frame {msg.header.stamp.sec}.{msg.header.stamp.nanosec}')

def main():
    rclpy.init()
    rclpy.spin(CameraNode())
