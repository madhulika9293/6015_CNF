import socket

def Main():

    HOST = '127.0.0.1'
    PORT = 5000

    s = socket.socket()
    s.connect((HOST, PORT))
    message = input("-->")
    while  message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
        print("Recieved from server:" + str(data.decode()))
        message = input("-->")
    conn.close()

if __name__ == '__main__':
    Main()
