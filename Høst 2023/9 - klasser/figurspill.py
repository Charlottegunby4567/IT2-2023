import pygame
from figur import Figur

class Spiller(Figur):
    def __init__(self, bildesti: str, x: int, y: int) -> None:
        super().__init__(bildesti, x, y)
        self.navn = navn

class Fiende(Figur):
    def __init__(self, bildesti: str, x: int, y: int) -> None:
        super().__init__(bildesti, x, y)
        self.antall_liv = 100

# 1. Oppsett

pygame.init()
BREDDE = 500
HOYDE = 500
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()


while True:

# 2. Håndter input

    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

# 3. Oppdater spill

# 4. Tegn

    pygame.display.flip()
    klokke.tick(FPS)