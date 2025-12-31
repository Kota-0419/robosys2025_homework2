#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kota Matsura <s24c1110qm@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Monitor(Node):
    
    def __init__(self):
        super().__init__('monitor')
        self.subscription = self.create_subscription(
            Int16,
            'temperature',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        if msg.data > 30:
            self.get_logger().warn(f'ALERT: Too Hot! ({msg.data} C)')
        else:
            self.get_logger().info(f'Temperature: {msg.data} C')


def main(args=None):
    rclpy.init(args=args)
    node = Monitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
