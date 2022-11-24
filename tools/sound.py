"""
This file is a part of of My-PyChess application.

In this file, we handle all sound related stuff.
"""

import os.path
import time

try:
    import pygame.mixer
    pygame.mixer.init()
    
    SUCCESS = pygame.mixer.get_init() is not None

except (ImportError, RuntimeError):
    SUCCESS = False

if SUCCESS:
    click = pygame.mixer.Sound(os.path.join("res", "sounds", "click.ogg"))
    move = pygame.mixer.Sound(os.path.join("res", "sounds", "move.ogg"))
    start = pygame.mixer.Sound(os.path.join("res", "sounds", "start.ogg"))
    drag = pygame.mixer.Sound(os.path.join("res", "sounds", "drag.ogg"))

    background = pygame.mixer.Sound(os.path.join("res", "sounds", "background.ogg"))


