import pygame

class Planet:
    def __init__ (self, x, y, radius, bilde):
        self.x = x
        self.y = y
        self.radius = radius
        self.surface = pygame.image.load(bilde)
        self.surface = pygame.transform.scale(self.surface, (2 * self.radius, 2 * self.radius))

    def tegn(self, vindu):
        # pygame.draw.circle(vindu, "red", (self.x, self.y), self.radius)
        vindu.blit(self.surface, (self.x, self.y))

# 1. Oppsett
pygame.init()
BREDDE = 1200
HOYDE = 1000
FPS = 60
vindu = pygame.display.set_mode ((BREDDE, HOYDE))
klokke = pygame.time.Clock()

planeter = [
    Planet(-525, 20, 400, "bilder/sun.png"),
    Planet(200, 350, 25, "bilder/mercury.png"),
    Planet (250, 325, 50, "bilder/venus.png"),
    Planet (350, 300, 75, "bilder/earth.png"),
    Planet (525, 325, 50, "bilder/mars.png"),
    Planet(600, 200, 175, "bilder/jupiter.png"),
    Planet (900, 200, 150, "bilder/saturn.png"),
    Planet (1200, 300, 75, "bilder/uranus.png"),
    Planet (1350, 275, 100, "bilder/neptune.png"),
    Planet (1600, 350, 25, "bilder/moon.png")
]




while True:
    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    # 3. Oppdater spill

    # 4. Tegn
    for p in planeter:
        p.tegn(vindu)
    
    
    
    
    pygame.display.flip()
    klokke.tick(FPS)