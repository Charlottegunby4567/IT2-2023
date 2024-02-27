import pygame

class Tilstand():
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        self.overflate = pygame.Surface((vindu_bredde, vindu_høyde))
        self.ramme = self.overflate.get_rect()
        self.ramme.x = 0
        self.ramme.y = 0
        
