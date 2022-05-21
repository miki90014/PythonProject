import pickle
import socket
from _thread import *

from Server.methods import Game
from Server.variablesServer import SERVER, PORT, BITS

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    str(e)


s.listen(2)
print("Waiting for connection")
connected = set()
games = {}
idCount = 0




currentId = "0"

def threaded_client(conn, player, gameId):
    global idCount

    variable = games[gameId].data

    conn.send(str.encode(str(player)))

    reply = ""
    while True:
        try:
            data = conn.recv(BITS)
            data = pickle.loads(data)
            #print(type(data))

            if gameId in games:
                #games[gameId].printData()
                games[gameId].updateDate(data, player)
                #print("Po update:")
                #games[gameId].printData()


                if not data:
                    print("Disconnected")
                    break

                else:
                    print(player)
                    if player == 0:
                        reply = games[gameId].data[1]
                    else:
                        reply = games[gameId].data[0]

                    print("Recieved: ", data)
                    print("Sending: ", reply)

                conn.send(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: " + str(addr))

    idCount += 1
    currentPlayer = 0
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        currentPlayer = 1

    start_new_thread(threaded_client, (conn, currentPlayer, gameId))
    currentPlayer += 1

    #start_new_thread(threaded_client, (connection,))


