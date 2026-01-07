#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kota Matsura <s24c1110qm@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

ros2 launch robosys2025_homework2 talk_listen.launch.py > /dev/null 2>&1 &

sleep 5

timeout 10 ros2 topic echo /temperature | grep "data:"
ret=$?

killall ros2

if [ $ret -eq 0 ]; then
    echo "Test Passed: Temperature data received."
    exit 0
else
    echo "Test Failed: No temperature data received."
    exit 1
fi
