#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MovementNode(Node):
    def __init__(self):
        super().__init__('movement_node')
        self.cmd_topic = self.declare_parameter('cmd_topic', '/cmd_vel').value
        self.speed      = self.declare_parameter('speed', 0.2).value
        self.publisher  = self.create_publisher(Twist, self.cmd_topic, 10)
        self.timer      = self.create_timer(1.0, self.move)

    def move(self):
        msg = Twist()
        msg.linear.x = self.speed
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing speed {self.speed} m/s')

def main():
    rclpy.init()
    rclpy.spin(MovementNode())
