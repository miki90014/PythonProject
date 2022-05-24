import pygame

from client.enemy import SimpleEnemy, EnemyBullet, SuperEnemy
from client.variables import WIDTH, HEIGHT, VEL
#LOSE_HEALTH, POWERUP, VEL


def handleBullets(player, bullets, enemies, eBullets):
    for bullet in bullets:
        if bullet.x + bullet.width > WIDTH:
            player.bullets.remove(bullet)
        for enemy in enemies:
            if bullet.rect.colliderect(enemy):
                enemy.health -= 1
                if bullet in player.bullets:
                    player.bullets.remove(bullet)
                if enemy.health == 0:
                    player.score += enemy.points
                    enemies.remove(enemy)
    for eBullet in eBullets:
        if eBullet.x + eBullet.width > WIDTH:
            eBullets.remove(eBullet)
        if eBullet.rect.colliderect(player):
            player.health -=1
            eBullets.remove(eBullet)
    return enemies, eBullets


def handlePowerUp(player, powerUps):
    for powerUp in powerUps:
        if powerUp.x + powerUp.width < 0 or powerUp.y < 0 or powerUp.y > HEIGHT:
            powerUps.remove(powerUp)
        if player.rect.colliderect(powerUp):
            powerUp.doSth(player)
            #POWERUP.play()
            powerUps.remove(powerUp)
    return powerUps

def changeDificulty(player, basicVelB, basicVeleB, basicVelE, basicVelSE, basicVelSupE, basicVelPUp):
    basicVelB *= VEL
    basicVeleB *= VEL
    basicVelE *= VEL
    basicVelSE *= VEL
    basicVelSupE *= VEL
    basicVelPUp *= VEL
    player.changeVel()
    return basicVelB, basicVeleB, basicVelE, basicVelSE, basicVelSupE, basicVelPUp



def handleEnemies(player, enemies):
    for enemy in enemies:
        if enemy.x + enemy.width < 0 or enemy.y < 0 or enemy.y > HEIGHT:
            enemies.remove(enemy)
        if player.rect.colliderect(enemy):
            player.health -=1
            #LOSE_HEALTH.play()
            pygame.event.post(pygame.event.Event(player.hit))
            enemies.remove(enemy)
    return enemies

def createEBullets(enemies, eBullets, seconds, basicVeleB):
    for enemy in enemies:
        if isinstance(enemy, SimpleEnemy):
            if seconds % 2 == 0:
                eBullets.append(EnemyBullet((0, 255, 0), enemy, basicVeleB))
        elif isinstance(enemy, SuperEnemy):
                eBullets.append(EnemyBullet((0, 0, 255), enemy, basicVeleB))
    return eBullets