import pygame

from client.Enemy import SimpleEnemy, EnemyBullet
from client.variables import WIDTH, HEIGHT


def handleBullets(player, bullets, enemies, eBullets):
    for bullet in bullets:
        if bullet.x + bullet.width >WIDTH:
            player.bullets.remove(bullet)
        for enemy in enemies:
            if bullet.rect.colliderect(enemy):
                enemy.health -=1
                if enemy.health==0:
                    player.score+=enemy.points
                    enemies.remove(enemy)
                    player.bullets.remove(bullet)
    for eBullet in eBullets:
        if eBullet.x + eBullet.width >WIDTH:
            eBullets.remove(eBullet)
        if eBullet.rect.colliderect(player):
            player.health -=1
            eBullets.remove(eBullet)
    return enemies, eBullets

#Do dodania
#def handlePowerUp(player, benefits):
#    for benefit in benefits:
#        if benefit.x - benefit.width < WIDTH or benefit.y - benefit.height < HEIGHT:
#            benefits.remove(benefit)
#        if player.rect.colliderect(benefit):
#            benefit.DoSth(player)
#            benefits.remove(benefit)
#    return benefits


def handleEnemies(player, enemies):
    for enemy in enemies:
        if enemy.x + enemy.width < 0 or enemy.y < 0 or enemy.y > HEIGHT :
            enemies.remove(enemy)
        if player.rect.colliderect(enemy):
            player.health -=1
            print(player.health)
            pygame.event.post(pygame.event.Event(player.hit))
            enemies.remove(enemy)
    return enemies

def createEBullets(enemies, eBullets):
    for enemy in enemies:
        if isinstance(enemy, SimpleEnemy):
            eBullets.append(EnemyBullet((0,0,255),enemy))
    return eBullets