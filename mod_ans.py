# 1 - Import library
import math
import random
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
pygame.mixer.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100, 100]
acc = [0, 0]
arrows = []
badtimer = 100
badtimer1 = 0
badguys = [[640, 100]]
healthvalue = 194


# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

# 3.1 - Load audio
hit = pygame.mixer.Sound("resources/audios/explode.wav")
enemy = pygame.mixer.Sound("resources/audios/enemy.wav")
shoot = pygame.mixer.Sound("resources/audios/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('resources/audios/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


# 4 - keep looping through
running = 1
exitcode = 0
while running:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass, (x*100, y*100))
    for event in pygame.event.get():
        if event.type == QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
        if event.type == KEYUP:
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_RIGHT:
                keys[3] = False
        if event.type == QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == MOUSEBUTTONDOWN:
            shoot.play()
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append(
                [math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)), playerpos1[0] + 32,
                 playerpos1[1] + 32])
    # 9 - Move player
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
    badtimer -= 1
    # 10 - Win/Lose check
    if pygame.time.get_ticks() >= 90000:
        running = 0
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0] * 1.0 / acc[1] * 100
    else:
        accuracy = 0

# 11 - Win/lose display
if exitcode == 0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(gameover, (0, 0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(youwin, (0, 0))
    screen.blit(text, textRect)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
