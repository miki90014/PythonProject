import socket
from _thread import *
import sys

from Server.variablesServer import SERVER, PORT, BITS

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    str(e)


s.listen()
print("Waiting for connection")

def threaded_client(conn):

    conn.send(str.encode("Connected"))

    reply = ""
    while True:
        try:
            data = conn.recv(BITS) #amount of information we gonna recieve, to increase do "*8"
            reply = data.decode()

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break

    conn.send(str.encode("Disconnected"))
    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: " + str(addr))
    threaded_client(conn)

    #start_new_thread(threaded_client, (connection,))


