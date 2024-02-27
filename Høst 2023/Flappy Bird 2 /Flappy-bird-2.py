import pygame
import random

# Initialiserer pygame
pygame.init()

# Definerer vindusstørrelse
VINDU_BREDDE = 600
VINDU_HØYDE = 400
FPS = 40
klokke = pygame.time.Clock()
vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HØYDE))
pygame.display.set_caption("Flappy Bird")

# Definerer farger
HVIT = (255, 255, 255)
ROD = (255, 0, 0)
GRONN = (0, 255, 0)


pygame.display.update()
klokke.tick(FPS)