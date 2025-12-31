# robosys2025-home-work2

![test](https://github.com/Kota-0429/robosys2025-home-work2/actions/workflows/test.yml/badge.svg)

ROS 2を用いて、温度データの送受信と監視を行うパッケージです。

## 概要
* `sensor`: 温度データを模擬的に生成し、パブリッシュするノード
* `monitor`: 温度データをサブスクライブし、設定値（30℃）を超えた場合に警告を表示するノード

## 実行環境
* Ubuntu 22.04 LTS (Jammy Jellyfish)
* ROS 2 Humble Hawksbill

## ノードとトピック
### sensor
温度データ（16bit整数）を送信します。
* パブリッシュするトピック: `temperature` (std_msgs/msg/Int16)

### monitor
温度データを受信して端末に表示します。30度を超えると警告を出します。
* サブスクライブするトピック: `temperature` (std_msgs/msg/Int16)

## 使用法

ターミナルを2つ開き、それぞれで以下のコマンドを実行します。

**ターミナル1（受信側）**
```bash
ros2 run mypkg monitor

**ターミナル2（送信側）**
```bash
ros2 run mypkg sensor

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* ©2025 Kota Matsura
