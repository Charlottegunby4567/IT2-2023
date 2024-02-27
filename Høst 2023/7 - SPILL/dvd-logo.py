import pygame
import random

def tilfeldig_farge():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return [r , g , b]

# 1. oppsett (init)
pygame.init()     # starter opp pygame  
BREDDE = 1200   # er konstaant
HOYDE = 600

vindu = pygame.display.set_mode ([BREDDE,HOYDE])
klokke = pygame.time.Clock()        # Opretter en kokke, denne skalbrukes for å begrense spillet til 60FPS      

x = 20
y = 50
radius = 50
farge = tilfeldig_farge()   # 
x_fart = 1
y_fart = 1


spiller = True

while spiller:      # gameloop
    # 2. Håndtere input/hendelser

    hendelser = pygame.event.get()  # lager en liste med alle hendelsene
    for hendelse in hendelser:      # 
        if hendelse.type == pygame.QUIT:
            spiller = False

    # 3. Oppdaterer spill
    x += x_fart
    y += y_fart
    if x > BREDDE or x < 0:     # treffer vegg på høyre side eller venstre side
        x_fart = x_fart * -1
        farge = tilfeldig_farge()
    if y > HOYDE or y < 0:     # treffer vegg på bunneen eller toppen
        y_fart = y_fart * -1
        farge = tilfeldig_farge()

    # 4. Tegn (render)
    vindu.fill([0,0,0])
    pygame.draw.circle(vindu, farge , [x, y], radius) #hvor den skal tegnes, [fargen], [kordinater (x og y)], radius
    pygame.draw.circle(vindu,[255, 255, 255], [50, 75], 30) 
    pygame.draw.circle(vindu,[255, 255, 255], [75, 25], 30) 
    pygame.display.update()

    klokke.tick(60) #forteller at løkka skal kjøre 60 ganger i sekundet (60FPS)