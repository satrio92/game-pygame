import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Racing Master')
icon = pygame.image.load('images\snowmobile.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('images\player.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x,y):
    screen.blit(playerImg,(x,y))

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                 playerX_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3


    player(playerX,playerY)
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
        

    pygame.display.update()
    

