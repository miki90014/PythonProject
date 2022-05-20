import pygame

from client.variables import WIDTH, HEIGHT, FILE


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
    def changeVel(self):
        self.vel = 1.1*self.vel

    def move(self, keys):

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