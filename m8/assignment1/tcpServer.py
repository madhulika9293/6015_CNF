import socket

def Main():

    HOST = '127.0.0.1'
    PORT = 5000

    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)
    print ('server is running....')
    conn, addr = s.accept()
    print ('Connected by', addr)

    Dict = {'INR' : 0, 'Dollar' : 1, 'Pounds' : 2,'Yen' : 3}
    matrix = [[1.0, 0.014, 0.011, 1.58], [72.1, 1.0, 0.79, 112.60], [89.98, 1.26, 1.0, 142.17], [0.63, 0.0089, 0.0070, 1.0]]

    while True:
        data = conn.recv(1024)
        if not data:
            break
        datalist = data.decode().split()
        value = float(matrix[int(Dict[datalist[1]])][int(Dict[datalist[4]])])
        currency = int(datalist[2]) * value
        conn.send((str(currency) + str(datalist[4])).encode())
    conn.close()

if __name__ == '__main__':
    Main()
