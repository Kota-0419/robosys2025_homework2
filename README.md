# robosys2025-home-work2

![test](https://github.com/Kota-0419/robosys2025-homework2/actions/workflows/test.yml/badge.svg)

ROS 2を用いて、温度データの送受信と監視を行うパッケージです。

## 概要
* `sensor`: 温度データを模擬的に生成し、パブリッシュするノード
* `monitor`: 温度データをサブスクライブし、設定値（30℃）を超えた場合に警告を表示するノード

## 実行環境
* Ubuntu 22.04 LTS (Jammy Jellyfish)
* ROS 2 Humble Hawksbill
* Python 3.10

## インストール
```bash
cd ~/ros2_ws/src
git clone [https://github.com/Kota-0419/robosys2025-homework2.git](https://github.com/Kota-0419/robosys2025-homework2.git)
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

## ノードとトピック
### sensor
温度データ（16bit整数）を送信します。
* パブリッシュするトピック: `temperature` (std_msgs/msg/Int16)

### monitor
温度データを受信して端末に表示します。設定値（デフォルト30℃）を超えると警告を出します。
* サブスクライブするトピック: `temperature` (std_msgs/msg/Int16)

## 使用法

### 1. 実行（一括起動）
Launchファイルを使用することで、sensorノードとmonitorノードを同時に起動できます。
※事前にビルドとsource（`source install/setup.bash`）が必要です。

```bash
ros2 launch robosys2025_homework2 talk_listen.launch.py
```
実行後、`Ctrl + C`で終了します。

### 2. パラメータの設定
monitorノードは、警告を出す温度のしきい値を変更できます（デフォルトは30℃）。

### 例：25℃で警告を出したい場合

```bash
ros2 run robosys2025_homework2 monitor --ros-args -p threshold:=25
```

### 3. 個別に実行する場合
従来通り、ターミナルを2つ開いて実行することも可能です。

### ターミナル1（受信側）

```bash
ros2 run robosys2025_homework2 monitor
```

### ターミナル2（送信側）

```bash
ros2 run robosys2025_homework2 sensor
```

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* ©2025 Kota Matsura
