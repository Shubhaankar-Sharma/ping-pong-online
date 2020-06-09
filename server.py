import socket
from _thread import *
from random import randint
import sys

import pickle


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

server = '192.168.1.3'
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))


except socket.error as e:
    str(e)

s.listen()
print("Waiting For a connection, Server Started")
v,y = randint(4, 8), randint(-8, 8)
while y ==0:
    y = randint(-8,8)
l = randint(-8,8)
players = [[[BLUE, 20, 90],[70,300],[v,y]],[ [BLUE, 20, 90],[870,300],[v,y]]]


# When Player initialy connects
def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player][1] = data[0]

            if not data:
                print("Disconnected")
                break

            else:
                if player == 1:
                    reply = players[0][1]

                else:
                    reply = players[1][1]

                print("Recieved: ", data)
                print("Sending:", reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost Connection")
    conn.close()


currentPlayer = 0
total = []
lst = []
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    total.append(addr)
    lst.append(conn)
    lst.append(addr)


    if len(total) >1:
        conn_1 = lst[0]
        addr_1 = lst[1]
        conn_2 = lst[2]
        addr_2 = lst[3]
        print(len(total))
        start_new_thread(threaded_client, (conn_1, currentPlayer))
        currentPlayer += 1
        start_new_thread(threaded_client, (conn_2, currentPlayer))

