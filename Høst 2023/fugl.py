import pygame

#1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

overskrift_font = pygame.font.SysFont("Arial", 32)
overskrift_surface = overskrift_font.render("Flappy Bird", True, "black")


fugl_surface = pygame.image.load("bilder/bird.jpg").convert_alpha()
fugl_surface = pygame.transform.scale_by(fugl_surface, 0.2)
fugl_rect = fugl_surface.get_rect()
fugl_rect.bottom = HOYDE
fugl_rect.centerx = BREDDE / 2
fugl_fart = 60

rør_surface = pygame.image.load("bilder/rør.jpg").convert_alpha()
rør_surface = pygame.transform.scale_by(rør_surface, 0.2)
rør_rect = rør_surface.get_rect()
rør_rect.bottom = 600


while True:
    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if hendelse.type == pygame.KEYDOWN:
            if hendelse.key == pygame.K_LEFT:
                spiller_fart = -1
            elif hendelse.key == pygame.K_RIGHT:
                spiller_fart = 1
        if hendelse.type == pygame.KEYUP:
            spiller_fart = 0


    # 3. Oppdater spill
    rør_rect.left -= 1
    if rør_rect.right < 0:
        rør_rect.left = BREDDE
    
    fugl_rect.left += fugl_fart

    if fugl_rect.colliderect(rør_rect):
        pygame.quit()
        raise SystemExit
    
    
    # 4. Tegn
    vindu.fill ("white")
    vindu.blit(overskrift_surface, (10, 10))

    vindu.blit(fugl_surface, fugl_rect)
    vindu.blit(rør_surface, rør_rect)

    pygame.display.flip()
    klokke.tick(FPS)
