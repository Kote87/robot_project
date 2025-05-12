    
    #!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ExplorationNode(Node):
    def __init__(self):
        super().__init__('exploration_node')

        self.declare_parameter('linear_speed', 0.25)
        self.declare_parameter('min_distance', 0.35)

        self.linear_speed = self.get_parameter('linear_speed').value
        self.min_distance = self.get_parameter('min_distance').value

        self.create_subscription(
            LaserScan, '/scan', self.scan_callback, 10)

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('Exploration node started')

    # ---------- NUEVO algoritmo ----------
    def scan_callback(self, msg: LaserScan):
        total = len(msg.ranges)
        width = int(total * 15 / 360)        # ±15 °

        front = msg.ranges[:width] + msg.ranges[-width:]
        front = [r for r in front             # descarta Inf/NaN
                 if not math.isinf(r) and not math.isnan(r)]

        min_front = min(front) if front else float('inf')

        twist = Twist()
        if min_front < self.min_distance:
            twist.angular.z = 0.6            # gira
        else:
            twist.linear.x = self.linear_speed

        self.cmd_pub.publish(twist)
    # -------------------------------------

def main():
    rclpy.init()
    node = ExplorationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
