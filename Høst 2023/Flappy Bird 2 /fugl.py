import pygame
from pygame.locals import Rect

class Fugl:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hopp_hastighet = 10
        self.fall_hastighet = 0
        self.høyde = 50
        self.bredde = 50
        self.bilde = pygame.image.load("fugl-kopi.png")  # Endre dette til banens bane

    def hopp(self):
        self.fall_hastighet = -self.hopp_hastighet

    def oppdater(self, tast):
        if tast[pygame.K_UP]:
            self.hopp()

        self.fall_hastighet += 1
        self.y += self.fall_hastighet

    def kollisjon(self, rør):
        fugl_rektangel = Rect(self.x, self.y, self.bredde, self.høyde)
        rør_rektangel = Rect(rør.x, rør.y, rør.bredde, rør.høyde)
        return fugl_rektangel.colliderect(rør_rektangel)

    def passerer_mellomrom(self, rør):
        return self.x > rør.x + rør.bredde

    def tegn(self, vindu):
        vindu.blit(self.bilde, (self.x, self.y))
     