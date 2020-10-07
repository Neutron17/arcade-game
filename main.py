import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Henlo")
icon = pygame.image.load("Java.png")
background = pygame.image.load("bgImg1.jpg")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("space-invaders.png")
playerX = 350
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("ufo(1).png"))
    enemyX.append(random.randint(0, 737))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(40)

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bulletState = "ready"

score_value = 0
font = pygame.font.Font("Roboto-Bold.ttf",32)

textX = 10
textY = 10

over_font = pygame.font.Font("Roboto-Bold.ttf",64)

def show_store(x,y):
    score = font.render("Score: " + str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200,250))

def player(x, y):
    screen.blit(playerImg, (int(x), y))

def enemy(x, y,i):
    screen.blit(enemyImg[i], (int(x), y))

def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (int(x + 16), int(y + 10)))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 1.5
        if event.key == pygame.K_RIGHT:
            playerX += 1.5
        if event.key == pygame.K_SPACE:
            if bulletState is "ready":
                bulletX = playerX
                fireBullet(bulletX, bulletY)

        if event.key == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = -2

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 735

    for i in range(num_of_enemy):

        if enemyY[i] > 440:
            for j in range(num_of_enemy):
                enemyY[i] = 2000
                game_over_text()
                break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 737)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i],i)

    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"
    if bulletState is "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_store(textX,textY)
    pygame.display.update()
