#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdometrySubscriber(Node):
    def __init__(self):
        super().__init__('odometry_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            'odometry/filtered',
            self.odometry_callback,
            10
        )
        self.subscription  # Prevent unused variable warning

    def odometry_callback(self, msg):
        pose = msg.pose.pose
        position = pose.position
        orientation = pose.orientation
        self.get_logger().info(f"Pose: Position ({position.x}, {position.y}), Orientation ({orientation.z}, {orientation.w})")

def main(args=None):
    rclpy.init(args=args)
    odometry_subscriber = OdometrySubscriber()
    rclpy.spin(odometry_subscriber)
    odometry_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
