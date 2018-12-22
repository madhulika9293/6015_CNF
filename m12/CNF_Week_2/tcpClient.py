import socket
from threading import *
import os,signal

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    print("Connected")
    thread2 = Thread(target = send, args = (s,)).start()

    while True:
        data = s.recv(1024).decode()
        # if(active_count() == 0):
            # s.close()
        print(data)
        if(data == "ATTENDANCE-SUCCESS"):
            # s.close()
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
            break

def send(s):
    while True:
        msg = input()
        s.send(msg.encode())

if __name__ == '__main__':
    Main()
