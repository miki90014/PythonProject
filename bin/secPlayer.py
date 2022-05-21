import pygame

from client.player import Player
from client.variables import WIDTH, HEIGHT


class SecPlayer(Player):
    def __init__(self, x, y, width, height, color):
        super(SecPlayer, self).__init__(x, y, width, height, color)

    def move(self, keys):

        if keys[pygame.K_a]:
            self.x -= self.vel
            if self.border():
                self.x=0
        if keys[pygame.K_d]:
            self.x += self.vel
            if self.border():
                self.x=WIDTH-self.width
        if keys[pygame.K_w]:
            self.y -= self.vel
            if self.border():
                self.y=0
        if keys[pygame.K_s]:
            self.y += self.vel
            if self.border():
                self.y=HEIGHT-self.height


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

def handleBullets(player1, player2, bullets1, bullets2, enemies, eBullets):
    for bullet in bullets1:
        if bullet.x + bullet.width >WIDTH:
            player1.bullets.remove(bullet)
        for enemy in enemies:
            if bullet.rect.colliderect(enemy):
                enemy.health -=1
                if enemy.health==0:
                    player1.score+=enemy.points
                    enemies.remove(enemy)
                    player1.bullets.remove(bullet)

    for bullet in bullets2:
        if bullet.x + bullet.width >WIDTH:
            player2.bullets.remove(bullet)
        for enemy in enemies:
            if bullet.rect.colliderect(enemy):
                enemy.health -=1
                if enemy.health==0:
                    player2.score+=enemy.points
                    enemies.remove(enemy)
                    player2.bullets.remove(bullet)

    for eBullet in eBullets:
        if eBullet.x + eBullet.width >WIDTH:
            eBullets.remove(eBullet)
        if eBullet.rect.colliderect(player1):
            player1.health -=1
            eBullets.remove(eBullet)
        if eBullet.rect.colliderect(player2):
            player2.health -=1
            eBullets.remove(eBullet)

    return enemies, eBullets

def handleEnemies(player1, player2, enemies):
    for enemy in enemies:
        if enemy.x + enemy.width < 0 or enemy.y < 0 or enemy.y > HEIGHT :
            enemies.remove(enemy)
        if player1.rect.colliderect(enemy):
            player1.health -=1
            pygame.event.post(pygame.event.Event(player1.hit))
            enemies.remove(enemy)
        elif player2.rect.colliderect(enemy):
            player2.health -=1
            pygame.event.post(pygame.event.Event(player2.hit))
            enemies.remove(enemy)
    return enemies