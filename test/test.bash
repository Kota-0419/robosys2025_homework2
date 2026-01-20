#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Kota Matsura
# SPDX-License-Identifier: BSD-3-Clause

ng () {
      echo ${1}行目が違うよ
      res=1
}

res=0

export PYTHONUNBUFFERED=1

source /opt/ros/humble/setup.bash

colcon build --symlink-install --packages-select robosys2025_homework2 || ng "$LINENO"
source install/setup.bash

timeout 10 ros2 run robosys2025_homework2 sensor > /tmp/robosys2025_homework2.log 2>&1 || true

cat /tmp/robosys2025_homework2.log

count=$(grep -c "Publishing" /tmp/robosys2025_homework2.log)

[ "$count" -ge 1 ] || ng "$LINENO"

[ "$res" = 0 ] && echo OK

exit $res
