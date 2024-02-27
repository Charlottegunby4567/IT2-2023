import pygame
import random
from spiller import Spiller
from fiende import Fiende

pygame.init()

# Skjermstørrelse
BREDDE, HØYDE = 800, 600
vindu = pygame.display.set_mode((BREDDE, HØYDE))
pygame.display.set_caption("Skytespill")

# Last inn bilder
bakgrunnsbilde = pygame.image.load("bakgrunn.png")
bakgrunnsbilde = pygame.transform.scale(bakgrunnsbilde, (BREDDE, HØYDE))

spiller_bilde = pygame.image.load("mario.png")
spiller_bredde, spiller_høyde = 80, 80
spiller_bilde = pygame.transform.scale(spiller_bilde, (spiller_bredde, spiller_høyde))

fiende_bilde = pygame.image.load("enemy.png")
fiende_bredde, fiende_høyde = 80, 80
fiende_bilde = pygame.transform.scale(fiende_bilde, (fiende_bredde, fiende_høyde))

# Opprett spiller og fiende objekter
spiller = Spiller(BREDDE // 2 - spiller_bredde // 2, HØYDE - spiller_høyde - 10, spiller_bredde, spiller_høyde, 10)
fiender = []

# ...

# Spillhovedløkke
klokke = pygame.time.Clock()
kjører = True
while kjører:
    klokke.tick(30)

    # Håndterer hendelser
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjører = False

    tast = pygame.key.get_pressed()

    # Beveg spilleren
    if tast[pygame.K_LEFT]:
        spiller.beveg_venstre()
    if tast[pygame.K_RIGHT]:
        spiller.beveg_høyre(BREDDE)  # Legg til BREDDE som et argument her

    # Oppdater fiender
    for fiende in fiender:
        fiende.beveg_ned()

        # Sjekk kollisjon med spiller
        spiller_rektangel = pygame.Rect(spiller.x, spiller.y, spiller.bredde, spiller.høyde)
        fiende_rektangel = pygame.Rect(fiende.x, fiende.y, fiende.bredde, fiende.høyde)
        if spiller_rektangel.colliderect(fiende_rektangel):
            kjører = False
        elif fiende.y > HØYDE:
            spiller.poeng += 1
            fiender.remove(fiende)

    # Legg til nye fiender med en sannsynlighet på 2%
    if random.randint(1, 50) == 1:
        fiende_x = random.randint(0, BREDDE - fiende_bredde)
        fiende_y = -fiende_høyde
        ny_fiende = Fiende(fiende_x, fiende_y, fiende_bredde, fiende_høyde, random.randint(2, 5))
        fiender.append(ny_fiende)

    # Tegn bakgrunnen
    vindu.blit(bakgrunnsbilde, (0, 0))

    # Tegn spilleren og fiendene
    vindu.blit(spiller_bilde, (spiller.x, spiller.y))
    for fiende in fiender:
        vindu.blit(fiende_bilde, (fiende.x, fiende.y))

    # Vis poengsum på skjermen
    font = pygame.font.SysFont(None, 30)
    poeng_text = font.render("Poeng: " + str(spiller.poeng), True, (0, 0, 0))
    vindu.blit(poeng_text, (10, 10))

    pygame.display.update()

pygame.quit()
