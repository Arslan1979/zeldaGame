import pygame.image
from grid import *

class LINK:
    def __init__(self):
        self.SPRITE_POS = pygame.image.load('./sprites/link/link_f6.png')
        self.PLAYER_POS = [0, 0]
        self.PLAYER_INV = []
        self.WEAPON = False
        self.HEALTH = 100
        self.MANA = 200
        self.DIRECTION = False

