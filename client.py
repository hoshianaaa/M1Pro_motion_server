# -*- coding : UTF-8 -*-

# 0.ライブラリのインポートと変数定義
import socket
import os
import struct
import ctypes
import time

class PacketMoveXYZR(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_float),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("r", ctypes.c_float),
    ]


class PacketPomp(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_float),
        ("pwr", ctypes.c_float),
        ("dir", ctypes.c_float),
    ]


target_ip = "192.168.2.6"
target_port = 6001
buffer_size = 300000

# 1.ソケットオブジェクトの作成
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.サーバに接続
tcp_client.connect((target_ip,target_port))


def move_xyz(x,y,z,r):

    # 3.サーバにデータを送信
    data = PacketMoveXYZR(1,x,y,z,r)
    tcp_client.send(data)

    # 4.サーバからのレスポンスを受信
    response = tcp_client.recv(300)
    print("[*]Received a response : {}".format(response))

def pomp(p,d):

    # 3.サーバにデータを送信
    data = PacketPomp(2,p,d)
    tcp_client.send(data)

    # 4.サーバからのレスポンスを受信
    response = tcp_client.recv(300)
    print("[*]Received a response : {}".format(response))


x = 200
x2 = 300
y = 0
z = 90

#move_xyz(x,y,z,0)

while True:
  move_xyz(x,y,z,0)
  move_xyz(x2,y,z,0)
