import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

background = pygame.image.load("images\mybackground.png")

pygame.display.set_caption('Racing Master')
icon = pygame.image.load('images\snowmobile.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('images\player.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = pygame.image.load('images\enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 10

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                 playerX_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

    player(playerX,playerY)
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    
    enemy(enemyX,enemyY)
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    if enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    pygame.display.update()
    

