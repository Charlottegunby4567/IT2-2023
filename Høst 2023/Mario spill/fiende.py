import pygame

class Fiende:
    def __init__(self, x, y, bredde, høyde, fart):
        self.x = x
        self.y = y
        self.bredde = bredde
        self.høyde = høyde
        self.fart = fart

    def beveg_ned(self):
        self.y += self.fart
