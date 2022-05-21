import pickle
import socket
import sys

from Server.variablesServer import SERVER, PORT, BITS


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER
        self.port = PORT
        self.addr = (self.server, self.port)
        self.number = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(BITS).decode()
        except:
            pass

    def send(self, data):
        try:
            #self.connect()
            self.client.send((pickle.dumps(data)))
            etwas = pickle.loads(self.client.recv(BITS))
            print(type(etwas))
            return etwas
        except socket.error as e:
            print(e)