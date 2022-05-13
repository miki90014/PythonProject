from types import NoneType

import pygame
import time
import random
from threading import Thread

from abc import ABC

WIDTH = 900
HEIGHT = 500
FPS = 80

bg = pygame.image.load("images\\background2.jpg")
bg = pygame.transform.scale(bg, (900,500))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

ONE = pygame.image.load("images\\Inkedbackground2ONE.jpg")
ONE = pygame.transform.scale(ONE, (900,500))
TWO = pygame.image.load("images\\Inkedbackground2TWO.jpg")
TWO = pygame.transform.scale(TWO, (900,500))
THREE = pygame.image.load("images\\Inkedbackground2THREE.jpg")
THREE = pygame.transform.scale(THREE, (900,500))
START = pygame.image.load("images\\Inkedbackground2START.jpg")
START = pygame.transform.scale(START, (900,500))

MAX_ENEMIES = 3
enemies = []

#COUNTING_SOUND = pygame.mixer.Sound("sound\\count.mp3")

#spaceship =

clientNumber = 0

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

#def SuperEnemy(Enemy):

def Asteroid(Enemy):
    def __init__(self, vel, width, height, color):
        super().__init__(self, vel, width, height, color)

#def SimpleEnemy(Enemy):

class Bullet():
    def __init__(self, color, player, WIN):
        self.color = color
        self.player = player
        self.x = player.x+player.width
        self.y = player.y+player.height/2
        self.width =10
        self.height = 3
        self.vel = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.x += self.vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Player():
    def __init__(self, x, y, width, height, color):
        self.x=x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 7
        self.rect = pygame.Rect(x,y,width,height)
        self.bullets = []
        self.maxBullets = 3
        self.hit = pygame.USEREVENT+1
        self.score = 0
        self.health = 3

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, self.rect)

    def border(self):
        if self.x+self.width>WIDTH or self.y+self.height>HEIGHT or self.x<0 or self.y<0:
            return True
        return False

    def move(self, keys):
         #dictionary of keys that player typed

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            if self.border():
                self.x=0
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            if self.border():
                self.x=WIDTH-self.width
        if keys[pygame.K_UP]:
            self.y -= self.vel
            if self.border():
                self.y=0
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            if self.border():
                self.y=HEIGHT-self.height


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

def redrawWINdow(WIN, player, enemies):

    WIN.blit(bg, (0, 0))
    pygame.draw.rect(WIN, player.color, player.rect)
    for bullet in player.bullets:
        bullet.move()
        pygame.draw.rect(WIN, bullet.color, bullet.rect)
    print(len(enemies))
    for enemy in enemies:
        enemy.move()
        pygame.draw.rect(WIN, enemy.color, enemy.rect)
    pygame.display.update()

def counting(i):
    if(i==0):
        WIN.blit(THREE, (0, 0))
    elif i==1:
        WIN.blit(TWO, (0, 0))
    elif i==2:
        WIN.blit(ONE, (0, 0))
    else:
        WIN.blit(START, (0, 0))
    pygame.display.update()

def handleBullets(player, bullets, enemies):
    for bullet in bullets:
        if bullet.x + bullet.width >WIDTH:
            player.bullets.remove(bullet)
        for enemy in enemies:
            if bullet.rect.colliderect(enemy):
                player.score+=enemy.points
                enemies.remove(enemy)
                print(player.score)
    return enemies

#Do dodania
#def handleBenefits(player, benefits):
#    for benefit in benefits:
#        if benefit.x - benefit.width < WIDTH or benefit.y - benefit.height < HEIGHT:
#            benefits.remove(benefit)
#        if player.rect.colliderect(benefit):
#            benefit.DoSth(player)
#            benefits.remove(benefit)
#    return benefits


def handleEnemies(player, enemies):
    for enemy in enemies:
        if enemy.x + enemy.width < 0 or enemy.y - enemy.height < 0 or enemy.y - enemy.height > HEIGHT:
            print("REMOVING!")
            enemies.remove(enemy)
        if player.rect.colliderect(enemy):
            print("U TOUCHED!")
            player.health -=1
            print(player.health)
            pygame.event.post(pygame.event.Event(player.hit))
            enemies.remove(enemy)
    return enemies


def startGame():
    WIN.blit(bg, (0, 0))
    for i in range(4):
        counting(i)
        time.sleep(1)

def play():
    #startGame()
    global MAX_ENEMIES
    start_time = time.time()
    seconds = 0
    clock=pygame.time.Clock()
    run = True
    p = Player(50,50,40,40,(0,255,0))
    enemies = []
    while run:
        if seconds< (int)(time.time()-start_time):
            seconds = (int)(time.time()-start_time)
            enemies = spawnEnemy(seconds, enemies)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(p.bullets) < p.maxBullets:
                    bullet = Bullet((255,0,0),p, WIN)
                    p.bullets.append(bullet)
        keys = pygame.key.get_pressed()
        enemies = handleBullets(p, p.bullets, enemies)
        enemies = handleEnemies(p, enemies)
        p.move(keys)
        redrawWINdow(WIN, p, enemies)
    pygame.quit()


def spawnEnemy(seconds, enemies):
    global MAX_ENEMIES
    if seconds%3==0:
        MAX_ENEMIES += 1
    if len(enemies) <= MAX_ENEMIES:
        enemies.append(Enemy(7,50, 50,(255,0,0)))
        return enemies