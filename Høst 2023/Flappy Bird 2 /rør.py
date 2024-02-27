import pygame
from pygame.locals import Rect
import random

class Rør:
    def __init__(self, x):
        self.x = x
        self.høyde = random.randint(50, 400)
        self.mellomrom = 150
        self.bredde = 50
        self.passert = False
        self.bilde = pygame.image.load("rør-kopi.png")  # Endre dette til bildet av røret

    def oppdater(self):
        self.x -= 5

    def tegn(self, vindu, VINDU_HØYDE):
        # Tegner røret øverst
        vindu.blit(self.bilde, (self.x, 0, self.bredde, self.høyde))

        # Tegner røret nederst
        vindu.blit(self.bilde, (self.x, self.høyde + self.mellomrom, self.bredde, VINDU_HØYDE - self.høyde - self.mellomrom))
