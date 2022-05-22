import pygame

from client.enemy import Enemy, SimpleEnemy, SuperEnemy
from client.variables import BLACK, WHITE, WIDTH, HEIGHT, FPS, bg, END_QUIT, END_SCORE, END


def spawnEnemy(seconds, enemies):
    global MAX_ENEMIES
    if seconds%3==0:
        MAX_ENEMIES += 1
    if len(enemies) <= MAX_ENEMIES:
        enemies.append(Enemy(7, 50, 50, (0, 0, 0)))
        if len(enemies)== 1:
            enemies.append(SimpleEnemy(5,50, 50,(0,0,255), enemies[0].y))
        if(seconds%5==0):
            enemies.append(SuperEnemy(3, 50, 50, (0, 255, 0), enemies[0].y))
        return enemies

def drawEnd(WIN, player1, player2):
    width = 720
    height =200
    if player1.score>player2.score:
        text = "Player1 won!"
    elif player2.score>player1.score:
        text = "Player2 won!"
    else:
        text = "Withdraw!"
    Text = END.render(text, 1, (255, 255, 255))
    ScoreText1 = END_SCORE.render(
        "Score Player1: " + str(player1.score), 1, WHITE)
    ScoreText2 = END_SCORE.render(
        "Score Player2: " + str(player2.score), 1, WHITE)

    Return = END_QUIT.render("Menu", 1, WHITE)
    Quit = END_QUIT.render("Exit", 1, WHITE)

    clock = pygame.time.Clock()
    run = True

    buttonw = 370
    buttonh = 50
    buttonx = WIDTH / 18
    buttony = (HEIGHT / 1.2)
    padding = 400 + buttonx

    quitb = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    quitw = pygame.Rect(buttonx - 1, buttony - 1, buttonw + 2, buttonh + 2)

    buttonx += padding
    endb = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    endw = pygame.Rect(buttonx - 1, buttony - 1, buttonw + 2, buttonh + 2)

    while run:

        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()

        WIN.blit(bg, (0, 0))
        pygame.draw.rect(WIN, (255, 255, 255), ((WIDTH / 2 - width / 2) - 1, (HEIGHT / 2 - height / 2) - 1, width+2, height + 2))
        pygame.draw.rect(WIN, (0, 0, 0), (WIDTH/2-width/2, HEIGHT/2-height/2, width, height))
        WIN.blit(Text, (WIDTH/2-width/2 +10, HEIGHT/2-height/2 + 10))
        WIN.blit(ScoreText1, (WIDTH/2- 3*width/8, HEIGHT/2-height/2+120))
        WIN.blit(ScoreText2, (WIDTH / 2 - 3*width / 8, HEIGHT / 2 - height / 2 + 160))

        pygame.draw.rect(WIN, WHITE, quitw)
        pygame.draw.rect(WIN, BLACK, quitb)
        pygame.draw.rect(WIN, WHITE, endw)
        pygame.draw.rect(WIN, BLACK, endb)

        WIN.blit(Quit, (buttonx - padding + buttonw / 2 - 63, buttony + 5))
        WIN.blit(Return, (buttonx + buttonw / 2 - 63, buttony + 5))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if endb.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                #menu()
        if quitb.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()