#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class SensorListener(Node):
    def __init__(self):
        super().__init__('sensor_listener')
        self.scan_topic = self.declare_parameter('scan_topic', '/scan').value
        self.threshold  = self.declare_parameter('range_threshold', 0.5).value
        self.create_subscription(LaserScan, self.scan_topic, self.cb, 10)

    def cb(self, scan):
        if min(scan.ranges) < self.threshold:
            self.get_logger().warn('⚠️  Objeto cerca!')

def main():
    rclpy.init()
    rclpy.spin(SensorListener())
