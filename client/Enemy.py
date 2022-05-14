import random

import pygame

from Client.variables import WIDTH
from Client.variables import HEIGHT
from Client.variables import MAX_ENEMIES



class Enemy():
    def __init__(self, vel, width, height, color):
        self.x = WIDTH
        self.y = random.randint(0, HEIGHT-50)
        self.width = width
        self.height = height
        self.color = color
        self.vel = vel
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.points = 5
        self.health = 1

    def move(self):
        self.x -= self.vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def border(self):
        if self.x+self.width>WIDTH or self.y+self.height>HEIGHT or self.x<0 or self.y<0:
            return True
        return False

def SuperEnemy(Enemy):
    pass

def Asteroid(Enemy):
    def __init__(self, vel, width, height, color):
        super().__init__(self, vel, width, height, color)

def SimpleEnemy(Enemy):
    pass

class ABCBullet():
    pass

class EnemyBullet():
    pass


def spawnEnemy(seconds, enemies):
    global MAX_ENEMIES
    if seconds%3==0:
        MAX_ENEMIES += 1
    if len(enemies) <= MAX_ENEMIES:
        enemies.append(Enemy(7,50, 50,(0,0,0)))
        return enemies

