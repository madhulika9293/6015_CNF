import csv
import socket
import os
from threading import *
import time
import signal

filename = "data.csv"

rows = []
rollnumbers = []
dictQ = {}
dictA = {}

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)
        rollnumbers.append(row[0])
        dictQ[row[0]] = row[1]
        dictA[row[1]] = row[2]

# print(rollnumbers)
# print(dictQ)
# print(dictA)
# for row in rows:
    # print(row)
    # for col in row:
        # print(col)

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))
    print('server started.....')
    s.listen(10)


    while True:
        c, addr = s.accept()
        welcome = "Hello! Welcome to class. Please mark your attendance."
        c.send(welcome.encode())
        c.send('\nPlease Enter your Keyword: '.encode())
        conn = c.recv(1024)
        message = str(conn.decode())
        msg = message.split(" ")
        recRoll = msg[1]
        if msg[0] == "MARK-ATTENDANCE":
            Thread(target = attendance, args = (c, recRoll)).start()
    s.close()

def attendance(c, recRoll):
    # print(recRoll)
    # while True:
        # try:
            if recRoll in rollnumbers:
                # print("YES")
                while True:
                    # print("reached")
                    # print(recRoll)
                    Ques = dictQ[recRoll]
                    toS = "SECRETQUESTION-" + Ques
                    c.send(toS.encode())
                    r1 = c.recv(1024).decode().split(" ")
                    Ans = dictA[Ques]
                    if r1[1] == Ans:
                        c.send("ATTENDANCE SUCCESS".encode())
                        break
            else:
                c.send('ROLLNUMBER-NOTFOUND'.encode())
        # except:
            # continue

if __name__ == '__main__':
    main()
