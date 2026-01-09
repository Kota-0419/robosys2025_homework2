#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kota Matsura <s24c1110qm@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

ros2 run robosys2025_homework2 sensor &
NODE_PID=$!

sleep 5

ros2 topic echo /temperature --once --timeout 5 > /tmp/output.log

cat /tmp/output.log

if grep -q "[0-9]" /tmp/output.log; then
    echo "Test Passed: Output matches"
    kill $NODE_PID
    exit 0
else
    echo "Test Failed: Output does not match"
    kill $NODE_PID
    exit 1
fi
