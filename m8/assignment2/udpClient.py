import socket

def Main():

    HOST = '127.0.0.1'
    PORT = 5001
    server = ('127.0.0.1', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))

    message = input("-->")

    while  message != 'q':
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print("Recieved from server:" + str(data.decode()) + '\n')
        message = input("-->")
    s.close()

if __name__ == '__main__':
    Main()
