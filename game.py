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
badtimer1 = 100
badguys = [[640, 100]]
healthvalue = 194
wolves = [[640,100]]


# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
night = pygame.image.load("resources/images/new_background.jpg")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1
wolfimg = pygame.image.load("resources/images/wolf.png")
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
    screen.blit(night, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    #showing the bunny
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    # 6.2 - Draw arrows
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    #6.3 draw badgers / badguys
    if badtimer == 0:
        # adding new bad guys
        badguys.append([900, random.randint(50, 430)])

        badtimer = 100

    # remove bad guys once it's out of screen
    index = 0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)

        badguy[0] -= 5# moving the badguy to the left of scrreen

        # 6.3.1 - Attack castle
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            hit.play()
            healthvalue -= random.randint(5, 20)
            badguys.pop(index)

        # 6.3.2 - Check for collisions
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                enemy.play()
                acc[0] += 1
                badguys.pop(index)
                arrows.pop(index1)
            index1 += 1

        index += 1 #this goes to 6.3.3

    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    # 6.4
    # remove wolf once it's out of scrreen
        # 6.4 draw wolves / badguys
    if badtimer1 == 0:
        # adding new bad guys

        wolves.append([640, random.randint(50, 430)])
        badtimer1 = 100

    # remove bad guys once it's out of screen
    indexw = 0
    for wolf in wolves:
        if wolf[0] < -64:
            wolves.pop(index)

        wolf[0] -= 5  # moving the badguy to the left of scrreen

        # 6.4.1 - Attack castle
        badrect = pygame.Rect(wolfimg.get_rect())
        badrect.top = wolf[1]
        badrect.left = wolf[0]
        if badrect.left < 64:
            hit.play()
            healthvalue -= random.randint(5, 20)
            wolves.pop(indexw)

        # 6.4.2 - Check for collisions
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                enemy.play()
                acc[0] += 1
                wolves.pop(indexw)
                arrows.pop(index1)
            index1 += 1

        # 6.4.3 next wolf
        indexw += 1

    for wolf in wolves:
        screen.blit(wolfimg, wolf)

    # 9 - Move player
    if keys[0]:
        if playerpos[1]>10:
            playerpos[1] -= 5
    elif keys[2]:
        if playerpos[1] <470:
            playerpos[1] += 5
    if keys[1]:
        if playerpos[0] >10:
          playerpos[0] -= 5
    elif keys[3]:
        if playerpos[0] < 630:
         playerpos[0] += 5
    badtimer -= 1 #part that changes the timer
    badtimer1 -= 1

    pygame.display.flip()  # update the screen
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
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

