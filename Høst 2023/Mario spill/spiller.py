import pygame

class Spiller:
    def __init__(self, x, y, bredde, høyde, fart):
        self.x = x
        self.y = y
        self.bredde = bredde
        self.høyde = høyde
        self.fart = fart
        self.poeng = 0

    def beveg_venstre(self):
        if self.x > self.fart:
            self.x -= self.fart

    def beveg_høyre(self, BREDDE):
        if self.x < BREDDE - self.bredde - self.fart:
            self.x += self.fart

    def beveg_venstre(self):
        if self.x > self.fart:
            self.x -= self.fart

    def beveg_høyre(self, BREDDE):
        if self.x < BREDDE - self.bredde - self.fart:
            self.x += self.fart

