import socket
import os
from threading import *
import time
import signal

def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.bind((host,port))
	print('server started.....')
	s.listen(10)

	clients = []
	names = {}

	while True:
		c, addr = s.accept()
		welcome = "Hello all! Welcome to the group chat. Enter 'Bye' to exit"
		c.send(welcome.encode())
		c.send('\nPlease Enter your Name: '.encode())
		conn_name = c.recv(1024)
		print('Connected User: ' + conn_name.decode())
		names[c] = str(conn_name.decode())
		clients.append(c)
		for con in clients:
			if c != con:
				con.send((names[c] + ' is Connected.').encode())
		Thread(target = chatclients, args = (c, addr, clients, names)).start()
	s.close()


def check():
	print(active_count())
	if (active_count() == 2):
		print('Waiting for Connections....')
		time.sleep(10)
		if (active_count() == 2):
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)

def chatclients(c, addr, clients, names):
	while True:
		try:
			message = (c.recv(1024)).decode()
			print(names[c] + ' --> ' + message)
			if message != 'Bye' and c in clients:
				for client in clients:
					if c != client:
						try:
							name = names[c]
							client.send((name + '-->' + message).encode())
						except:
							c.close()
							remove(c, clients)
			else:
				c.send(('Do you want to Exit?(Y/N)').encode())
				if ((c.recv(1024)).decode() == 'Y'):
					for con in clients:
						if c != con:
							con.send((names[c] + ' is disconnected').encode())
					c.send('Disconnect'.encode())
					remove(c,clients)
					check()
					return 1
		except:
			continue
	c.close()

def remove(c, clients):
	if c in clients:
		clients.remove(c)


if __name__ == '__main__':
	Main()