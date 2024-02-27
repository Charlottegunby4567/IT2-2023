import pygame
import random

# 1. Oppsett
pygame.init()

# SPILLVINDU OG KLOKKE
BREDDE = 1280
HOYDE = 720
FPS = 80
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
stor_font = pygame.font.SysFont("Arial", 60)
liten_font = pygame.font.SysFont("Arial", 12)


dino_x = 300
dino_y = 300
dino_høyde = 100
dino_bredde = 100

dino_bilde1 = pygame.image.load ("bilder/dino1.png"). convert_alpha()

sirkel1_x = 800
sirkel1_y = 350
sirkel1_farge = "green"

sirkel2_x = 300
sirkel2_y = 500
sirkel2_farge = "green"



while True:
# Gameloop:

    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    # Input fra tastatur
    taster = pygame.key.get_pressed()
    if taster[pygame.K_RIGHT]:
        print("pil høyre")
        dino_x += 1

    if taster [pygame.K_LEFT]:
        print("pil venstre")
        dino_x -= 1
    
    if taster [pygame.K_UP]:
        print ("pil opp")
        dino_y -= 1
    
    if taster [pygame.K_DOWN]:
        print ("pil ned")
        dino_y += 1
    
    if taster [pygame.K_ESCAPE]:
        pygame.quit()
        raise SystemExit

    # Input fra mus
        # Klikk og posisjon
    mus = pygame.mouse.get_pressed()
    if mus [0]:
        mus_x, mus_y = pygame.mouse.get_pos()
        print (f"Venstreklikk: ({mus_x}, {mus_y})")






    # 3. Oppdater spill


    dino_rektangel = pygame.Rect(dino_x, dino_y, dino_bredde, dino_høyde)
    sirkel1_rektangel = pygame.Rect(sirkel1_x, sirkel1_y, 80, 80)
    sirkel2_rektangel = pygame.Rect(sirkel2_x, sirkel2_y, 80, 80)


    if dino_rektangel.colliderect (sirkel1_rektangel):
        print("Kollisjon sirkel 1!!")
        sirkel1_farge = "red"
        sirkel1_x = random.randint(0,BREDDE)
        sirkel1_y = random.randint (0,HOYDE)

    if dino_rektangel.colliderect (sirkel2_rektangel):
        print("Kollisjon sirkel 2!")
        sirkel2_farge = "red"
        sirkel2_x = random.randint(0,BREDDE)
        sirkel2_y = random.randint (0,HOYDE)
    



    # 4. Tegn
    vindu.fill("white")
    vindu.fill ((0, 0, 0))

    vindu.blit(dino_bilde1, (dino_x, dino_y))  # tegenr bildet i posisjonen (100,200)



    # sirkel 1
    pygame.draw.circle (vindu, sirkel1_farge, (sirkel1_x, sirkel1_y), 40)

    # sirkel 2
    pygame.draw.circle (vindu, sirkel2_farge, (sirkel2_x, sirkel2_y), 40)
    # pygame.draw.rect(vindu, (rød, grønn, blå), (x, y), radius)

    
    dino_tekst = stor_font.render ("DINO", True, "white")
    vindu.blit (dino_tekst, (550,100))
    
    

    pygame.display.flip()
    klokke.tick()