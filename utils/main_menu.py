import pygame
import sys

from utils.config import (blue, yellow, purple, white, black, screen_width, clock, FPS)
from utils.utils import text_format


def main_menu(screen):
    menu = True
    num = 0
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    num -= 1
                elif event.key == pygame.K_DOWN:
                    num += 1
                if event.key == pygame.K_RETURN:
                    calc = num % 3
                    if calc == 0:
                        difficulty_level = 1
                        return difficulty_level
                    elif calc == 1:
                        difficulty_level = 2
                        return difficulty_level
                    else:
                        difficulty_level = 0
                        pygame.quit()
                        return difficulty_level

        # Main Menu UI
        screen.fill(blue)
        font = pygame.font.SysFont(None, 24)
        title = text_format("Shooting Bunny Game", font, yellow)
        question = text_format("Please make a selection", font, purple)
        if num % 3 == 0:
            easy_start = text_format("EASY", font, white)
        else:
            easy_start = text_format("EASY", font, black)
        if num %3 == 1:
            difficult_start = text_format("DIFFICULT", font, white)
        else:
            difficult_start = text_format("DIFFICULT", font, black)
        if num %3 == 2:
            text_quit = text_format("QUIT", font, white)
        else:
            text_quit = text_format("QUIT", font, black)

        title_rect = title.get_rect()
        question_rect = question.get_rect()
        easy_rect = easy_start.get_rect()
        difficult_rect = difficult_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (question_rect[2]), 60))
        screen.blit(question, (screen_width / 2 - (question_rect[2]), 120))
        screen.blit(easy_start, (screen_width / 2 - (question_rect[2]-55), 300))
        screen.blit(difficult_start, (screen_width / 2 - (difficult_rect[2]+65), 330))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2]+90), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")
    return None
