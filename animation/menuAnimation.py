import random
import pygame

from client.player import Player
from client.variables import WIDTH, HEIGHT, SPACESHIP, FILE


class Ship(Player):
    def __init__(self, x, y, width, height, color):
        super(Ship, self).__init__(x, y, width, height, color)
        f = open(FILE, "r")
        self.movement = f.readlines()
        f.close()

    def move(self, x, y):
        self.x =int(x)
        self.y =int(y)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

def drawShip(WIN, ship, reader):
    x,y = (reader.move()).split(" ")
    ship.move(x, y)
    WIN.blit(SPACESHIP, ship.rect)


class ReadFile():
    def __init__(self, ship):
        self.line =0
        self.movement = ship.movement
        self.maxLine = len(ship.movement)

    def move(self):
        if self.line==self.maxLine:
            self.line = 0
        self.line+=1
        return self.movement[self.line-1]
