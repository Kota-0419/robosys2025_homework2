#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kota Matsura <s24c1110qm@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

ros2 launch robosys2025_home_work2 talk_listen.launch.py > /dev/null 2>&1 &

sleep 5

ros2 topic echo /temperature --once
ros2 topic echo /alert --once

echo "Test Finished"
killall ros2
