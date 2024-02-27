import pygame

class Fotballspiller():
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        self.bilde = pygame.image.load("bilder/haaland.png").convert_alpha()
        self.ramme = self.bilde.get_rect()
        self.poeng = 0
        self.liv = 10

        # setetr fotballspilleren i startposisjonen
        self.ramme.centerx = vindu_bredde/2
        self.ramme.bottom = vindu_høyde
    
    def flytt(self, dx: int):
        self.ramme.x += dx

    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.ramme)
        
