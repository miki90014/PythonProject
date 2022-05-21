import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5555
BITS = 2048


class gameDate():
    def __init__(self, player, enemies, enemyBullets, powerUps, playerNumber, end):
        self.player = player
        self.enemies = enemies
        self.enemyBullets = enemyBullets
        self.powerUps = powerUps
        self.playerNumber = playerNumber
        self.end = end

    def getPosition(self):
        return self.player.x, self.player.y

    def getScore(self):
        return self.player.score

    def getHealth(self):
        return self.player.health

    def quitGame(self):
        self.end = True

    def getPlayerNumber(self):
        return self.playerNumber


def updateData(data, data2):
    return data2

class PlayerData():
    def __init__(self, x, y, color, health, score, maxBullets,bullets):
        self.x = x
        self.y = y
        self.color = color
        self.health = health
        self.score = score
        self.maxBullets = maxBullets
        self.bullets = bullets

    def getXY(self):
        return self.x, self.y

    def addBullet(self, x, y):
        self.bullets.append(BulletsData(x, y, self))

    def removeBullet(self, index):
        self.bullets.remove(index)

class BulletsData():
    def __init__(self, x, y, color, player):
        self.x = x
        self.y = y
        self.color = color
        self.player = player

powerUps = []
enemyBullets = []
enemies = []
player1 = PlayerData(50, 100, (0,255,0), 3, 0, 3, [])
player2 = PlayerData(50, 200, (255,0,255), 3, 0, 3, [])
#player1 = Player(50,50,40,40,(0,255,0))
#player2 = Player(100, 50, 40, 40, (255, 0, 255))
STARTUPDATA = [gameDate(player1, enemies, enemyBullets, powerUps, 0, False), gameDate(player2, enemies, enemyBullets, powerUps, 1, False)]