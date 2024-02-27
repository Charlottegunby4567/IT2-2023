import pygame

#1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

overskrift_font = pygame.font.SysFont("Arial", 32)
overskrift_surface = overskrift_font.render("Erna vs. Jonas", True, "black")


spiller_surface = pygame.image.load("erna.png").convert_alpha()
spiller_surface = pygame.transform.scale_by(spiller_surface, 0.2)
spiller_rect = spiller_surface.get_rect()
spiller_rect.bottom = HOYDE
spiller_rect.centerx = BREDDE / 2
spiller_fart = 0

fiende_surface = pygame.image.load("jonas.png").convert_alpha()
fiende_surface = pygame.transform.scale_by(fiende_surface, 0.2)
fiende_rect = fiende_surface.get_rect()
fiende_rect.centerx = BREDDE / 2
fiende_rect.top = 100


twitter_surface = pygame.image.load("twitter.png").convert_alpha()
twitter_rect = twitter_surface.get_rect()
twitter_rect.top = fiende_rect.bottom
twitter_rect.centerx = fiende_rect.centerx
twitter_fart = 1



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
    fiende_rect.left -= 1
    if fiende_rect.right < 0:
        fiende_rect.left = BREDDE
    
    spiller_rect.left += spiller_fart
    twitter_rect.top += twitter_fart

    if twitter_rect.top > HOYDE:
        twitter_rect.top = fiende_rect.bottom
        twitter_rect.centerx = fiende_rect.centerx
        twitter_fart += 1


    if spiller_rect.colliderect(twitter_rect):
        pygame.quit()
        raise SystemExit
    
    
    # 4. Tegn
    vindu.fill ("white")
    vindu.blit(overskrift_surface, (10, 10))

    vindu.blit(spiller_surface, spiller_rect)
    vindu.blit(fiende_surface, fiende_rect)
    vindu.blit(twitter_surface, twitter_rect)

    pygame.display.flip()
    klokke.tick(FPS)
