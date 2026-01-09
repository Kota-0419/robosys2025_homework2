# SPDX-FileCopyrightText: 2025 Kota Matsura <s24c1110qm@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    sensor = launch_ros.actions.Node(
        package='robosys2025_homework2',
        executable='sensor',
    )
    monitor = launch_ros.actions.Node(
        package='robosys2025_homework2',
        executable='monitor',
    )

    return launch.LaunchDescription([
        sensor,
        monitor,
    ])
