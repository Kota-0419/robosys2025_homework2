#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kota Matsura <s24c1110qm@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, Bool


class Monitor(Node):
    def __init__(self):
        super().__init__('monitor')
        self.declare_parameter('threshold', 30)

        self.pub = self.create_publisher(Bool, 'alert', 10)

        self.sub = self.create_subscription(
            Int16, 'temperature', self.cb, 10
        )

    def cb(self, msg):
        limit = self.get_parameter('threshold').get_parameter_value().integer_value
        
        alert = Bool()
        if msg.data > limit:
            self.get_logger().warn(f'ALERT: Too Hot! ({msg.data} C)')
            alert.data = True
        else:
            alert.data = False
            
        self.pub.publish(alert)


def main():
    rclpy.init()
    node = Monitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()


if __name__ == '__main__':
    main()
