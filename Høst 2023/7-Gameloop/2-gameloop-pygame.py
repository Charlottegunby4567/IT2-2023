import pygame

# 1. Oppsett
pygame.init()

# SPILLVINDU OG KLOKKE
BREDDE = 1280
HOYDE = 720
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
stor_font = pygame.font.SysFont("Arial", 24)
liten_font = pygame.font.SysFont("Arial", 12)


dino_x = 300
dino_y = 300
dino_bilde1 = pygame.image.load ("bilder/dino1.png"). convert_alpha()


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



    # 4. Tegn
    vindu.fill("gray")
    vindu.fill ((0, 0, 0))

    vindu.blit(dino_bilde1, (dino_x, dino_y))  # tegenr bildet i posisjonen (100,200)
    pygame.draw.rect(vindu, (255, 200, 200), (200, 250, 70, 90))    # rektangel
    # pygame.draw.rect(vindu, (rød, grønn, blå, (x, y, bredde, høyde)))


    tekst_lykke_til = liten_font ("Lykke til!", True, "white")
    vindu.blit (tekst_lykke_til, (200,100))

    
    



    print("En ruunde i gameloopen")
    pygame.display.flip()
    klokke.tick()