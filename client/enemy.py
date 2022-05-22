import random

import pygame

from client.variables import WIDTH
from client.variables import HEIGHT



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
        if self.x+self.width > WIDTH or self.y+self.height > HEIGHT or self.x < 0 or self.y < 0:
            return True
        return False


class SimpleEnemy(Enemy):
    def __init__(self, vel, width, height, color, y):
        Enemy.__init__(self, vel, width, height, color)
        rand = random.randint(0, HEIGHT-height)
        while rand < y + self.height and rand > y - self.height:
            rand = random.randint(0, HEIGHT - height)
        self.y = rand

        self.points = 10
        self.timeShoot = 3

    def changeTimeShoot(self):
        self.timeShoot = self.timeShoot/2

    def changeMaxBullets(self):
        self.maxBullets += 1

class SuperEnemy(SimpleEnemy):
    def __init__(self, vel, width, height, color, y):
        SimpleEnemy.__init__(self, vel, width, height, color, y)
        self.points = 20
        self.health = 2
        self.up = True

    def move(self):
        self.x -= self.vel
        if not self.up:
            self.y -= self.vel
        if self.up:
            self.y += self.vel
        if self.y-self.height < 0:
            self.up = True
        if self.y+self.height > HEIGHT:
            self.up = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class EnemyBullet():
    def __init__(self, color, enemy, vel):
        self.color = color
        self.enemy = enemy
        self.x = enemy.x - enemy.width
        self.y = enemy.y + enemy.height / 2
        self.width = 10
        self.height = 3
        self.vel = vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.x -= self.vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


def spawnEnemy(seconds, enemies, basicVelE, basicVelSE, basicVelSupE, MAX_ENEMIES):
    if len(enemies) <= MAX_ENEMIES:
        enemies.append(Enemy(basicVelE, 50, 50, (0, 0, 0)))
        if len(enemies) == 1:
            enemies.append(SimpleEnemy(basicVelSE, 50, 50, (0, 0, 255), enemies[0].y))
        if seconds % 5 == 0:
            enemies.append(SuperEnemy(basicVelSupE, 50, 50, (0, 255, 0), enemies[0].y))
        return enemies

