#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kota Matsura <s24c1110qm@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class Sensor(Node):
    def __init__(self):
        super().__init__('sensor')
        self.publisher_ = self.create_publisher(Int16, 'temperature', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Int16()
        msg.data = random.randint(20, 40)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data} C')


def main(args=None):
    rclpy.init(args=args)
    node = Sensor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
