# mypkg

2021年度ロボットシステム学の課題2の製作物です。

実行すると、素数が小さい順から表示されます。

実行にはROSのインストールが必須になるので、あらかじめインストールしておいてください。

___


## 動作環境

- Raspberry Pi 4

- OS  :  ubuntu 20.04 server
 
___

## 使用方法

#### 【インストール】
以下のコマンドを実行してください。

```
$ git clone https://github.com/nakamutomo/mypkg.git

$ cd ~/mypkg/scripts/

$ chmod +x prime_count.py
```
___

#### 【実行】
 
ターミナルを二つ開いて、それぞれで以下のコードを実行してください。Ctrl+Cで終了することができます。
 ___
ターミナル1
```
$ roscore &
$ rosrun mypkg prime_count.py
```
ターミナル2 
```
$ rostopic echo /prime_count
```
___

## デモ動画

https://youtu.be/7U56nQfiZoU


___

## ライセンス
  [BSD 3-Clause "New" or "Revised" License](https://github.com/nakamutomo/mypkg/blob/master/LICENSE)
  

