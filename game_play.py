import pygame
import os
import sys

from utils.config import screen_width, screen_height
from utils.main_menu import main_menu
from utils.main_game import game

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Initialization
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

difficulty_level=0

while True:
    difficulty_level = main_menu(screen)
    if difficulty_level == 1:
        game(screen, health_value=500, speed_of_enemies=1, badtimer_initial=500)
    elif difficulty_level == 2:
        game(screen, health_value=200, speed_of_enemies=2, badtimer_initial=200)
    else:
        pygame.quit
        sys.exit(0)
