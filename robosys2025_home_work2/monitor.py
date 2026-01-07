#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kota Matsura <s24c1110qm@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class Monitor(Node):
    def __init__(self):
        super().__init__('monitor')
        self.declare_parameter('threshold', 30)

        self.sub = self.create_subscription(
            Int16, 'temperature', self.cb, 10
        )

    def cb(self, msg):
        threshold_param = self.get_parameter('threshold')
        limit = threshold_param.get_parameter_value().integer_value

        self.get_logger().info(f'Temperature: {msg.data} C')

        if msg.data > limit:
            self.get_logger().warn(f'ALERT: Too Hot! ({msg.data} C)')


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
