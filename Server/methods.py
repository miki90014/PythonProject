from Server.variablesServer import STARTUPDATA


class Game():
    def __init__(self, id):
        self.p1Gone = False
        self.p2Gone = False
        self.ready = False
        self.id = id
        self.data = STARTUPDATA

    def updateDate(self, data, player):
        self.data[player] = data

    def printData(self):
        for d in self.data:
            print(d.player)
            print(d.playerNumber)
            print(d.end)


    def getDate(self, player):
        return self.data[player]

    def checkEnd(self, player):
        return self.data[player].end
