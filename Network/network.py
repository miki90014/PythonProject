import socket

from Server.variablesServer import SERVER, PORT, BITS


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER
        self.port = PORT
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4096).decode()
        except:
            pass

    def send(self, data):
        try:
            self.connect()
            self.client.send(str.encode(data))
            return self.client.recv(BITS).decode()
        except socket.error as e:
            print(e)


#Testing
n = Network()
print(n.send("Hello"))
#print(n.send("Working"))