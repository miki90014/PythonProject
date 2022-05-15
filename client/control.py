import pygame

from client.variables import WIDTH, HEIGHT


def handleBullets(player, bullets, enemies):
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