#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Kota Matsura
# SPDX-License-Identifier: BSD-3-Clause

ng () {
      echo ${1}行目が違うよ
      res=1
}

res=0

# あなたの環境（Humble）に合わせて変更
source /opt/ros/humble/setup.bash

# パッケージをビルド（あなたのパッケージ名を指定）
colcon build --symlink-install --packages-select robosys2025_homework2 || ng "$LINENO"
source install/setup.bash

# ノードを10秒間実行して、出力をログファイルに保存
# （以前のログで ros2 run robosys2025_homework2 talker を実行していたため）
timeout 10 ros2 run robosys2025_homework2 talker > /tmp/robosys2025_homework2.log 2>&1 || true

# ログを表示（デバッグ用）
cat /tmp/robosys2025_homework2.log

# ログの中に "Publishing" という文字が含まれているかカウント
# （ログ出力例: [INFO] ...: Publishing: 22 C）
count=$(grep -c "Publishing" /tmp/robosys2025_homework2.log)

# 1回以上出力されていればOK
[ "$count" -ge 1 ] || ng "$LINENO"

[ "$res" = 0 ] && echo OK

exit $res
