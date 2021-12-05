from ctypes import POINTER, WINFUNCTYPE, windll
from ctypes.wintypes import BOOL, HWND, RECT
import pygame


def text_format(message, textFont, textColor):
    # render text
    newText = textFont.render(message, True, textColor)
    return newText


def get_window_center():
    # get our window ID:
    hwnd = pygame.display.get_wm_info()["window"]

    # Jump through all the ctypes hoops:
    prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
    paramflags = (1, "hwnd"), (2, "lprect")

    GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)

    # finally get our data!
    rect = GetWindowRect(hwnd)

    center = [(rect.left + rect.right) / 2, (rect.bottom + rect.top) / 2]
    return center
