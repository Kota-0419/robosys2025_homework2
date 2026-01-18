#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Kota Matsura
# SPDX-License-Identifier: BSD-3-Clause

ng () {
      echo ${1}行目が違うよ
      res=1
}

res=0

# 【追加】Pythonの出力をバッファリングさせない（すぐに表示させる）設定
export PYTHONUNBUFFERED=1

source /opt/ros/humble/setup.bash

# パッケージをビルド
colcon build --symlink-install --packages-select robosys2025_homework2 || ng "$LINENO"
source install/setup.bash

# ノードを起動（バックグラウンドではなくtimeoutで実行）
timeout 10 ros2 run robosys2025_homework2 sensor > /tmp/robosys2025_homework2.log 2>&1 || true

# ログの中身を確認（デバッグ用）
cat /tmp/robosys2025_homework2.log

# "Publishing" という文字が含まれているかカウント
count=$(grep -c "Publishing" /tmp/robosys2025_homework2.log)

# 1回以上出力されていればOK
[ "$count" -ge 1 ] || ng "$LINENO"

[ "$res" = 0 ] && echo OK

exit $res
