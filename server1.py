# 第1版python TCP server程序
# 实现server基本收发功能
# 实现TCP多线程收发
import socket
from time import ctime
import threading


# 多线程函数
def receive(c, a):
    print("链接地址：", str(a))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(ctime())
        print(data.decode('utf8'))  # 防止打印的字符前面带一个b
        c.send(data)
    print("连接", str(a), "断开！")
    c.close()
    # server.close()


# 创建socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""   # 本地端口
port = 9999
server.bind((host, port))

# 设置最大连接数，超过后排队
server.listen(5)
print("Waiting for connecting...")

while True:
    # 建立客户端连接
    client, address = server.accept()
    t = threading.Thread(target=receive, args=(client, address))
    t.start()
