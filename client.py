import pygame
import time
from threading import Thread

WIDTH = 900
HEIGHT = 500
FPS = 60

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

#spaceship =

clientNumber = 0


class Shooter():
    def __init__(self, color, player, WIN):
        self.color = color
        self.player = player
        self.x = player.x+player.width/2
        self.y = player.y+player.height/2
        self.width =10
        self.height = 3
        self.vel = 0.3
        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, self.rect)

    def move(self):
        self.x += self.vel
        self.rect = (self.x, self.y, self.width, self.height)

class Player():
    def __init__(self, x, y, width, height, color):
        self.x=x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 7                 #wartosc poruszania sie o ile krokow
        self.rect = (x,y,width,height)

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, self.rect)

    def border(self):
        if self.x+self.width>WIDTH or self.y+self.height>HEIGHT or self.x<0 or self.y<0:
            return True
        return False

    def shoot(self):
        self.sh = Shooter((255,0,0), self, WIN)
        while self.sh.x+self.sh.width<WIDTH:
            self.sh.move()
            redrawWINdow(WIN, self)
        del self.sh

    def move(self):
        keys = pygame.key.get_pressed() #dictionary of keys that player typed

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

        if keys[pygame.K_SPACE]:
            Thread(target = self.shoot()).start()
            #self.shoot()


        self.rect = (self.x, self.y, self.width, self.height)
        #print(str(self.x) + " " + str(self.y))

def redrawWINdow(WIN, player):


    WIN.blit(bg, (0, 0))
    player.draw(WIN)
    if hasattr(player, 'sh'):
        player.sh.draw(WIN)
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


def startGame():
    WIN.blit(bg, (0, 0))
    for i in range(4):
        counting(i)
        time.sleep(1)


def play():
    #startGame()
    clock=pygame.time.Clock()
    run = True
    p = Player(50,50,40,40,(0,255,0))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        #WIN.blit(bg, (0, 0))
        p.move()
        #Thread(target=p.move()).start()
        redrawWINdow(WIN, p)
        #print(str(p.x) +" "+ str(p.y))
    pygame.quit()

#if __name__ == '__main__':
#    play()