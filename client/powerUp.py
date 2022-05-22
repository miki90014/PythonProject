import pygame

from client.variables import WIDTH, HEIGHT, YELLOW, ORANGEYELLOW
import random


class powerUp():
    def __init__(self, vel, width, height):
        self.x = WIDTH
        self.x = WIDTH
        self.y = random.randint(0, HEIGHT - 50)
        self.width = width
        self.height = height
        self.color = YELLOW
        self.vel = vel
        self.rect = pygame.Rect(self.x, self.y, width, height)

    def move(self):
        self.x -= self.vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def doSth(self, player):
        pass

class Health(powerUp):
    def __init__(self, vel, width, height):
        powerUp.__init__(self, vel, width, height)

    def doSth(self, player):
        player.health += 1

class NewBullets(powerUp):
    def __init__(self, vel, width, height):
        powerUp.__init__(self, vel, width, height)
        self.color = ORANGEYELLOW

    def doSth(self, player):
        player.maxBullets += 1

def spawnPowerUp(seconds, powerUps, basicVelPUp):
    if seconds % 10 == 0:
        rand = random.randint(0, 2)
        if rand % 2 == 1:
            powerUps.append(Health(basicVelPUp, 50, 50))
        else:
            powerUps.append(NewBullets(basicVelPUp, 50, 50))
    return powerUps


