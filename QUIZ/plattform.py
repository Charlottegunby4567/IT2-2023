import pygame
import sys

# Initialiserer Pygame
pygame.init()

# Skjermstørrelse
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Farger
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Spillerattributter
player_width = 50
player_height = 50
player_x = 50
player_y = SCREEN_HEIGHT - player_height
player_velocity = 5

# Plattformattributter
platform_width = 100
platform_height = 20
platform_x = 350
platform_y = SCREEN_HEIGHT - platform_height - 50

# Oppretter skjermen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plattformspill")

# Spill-løkke
running = True
while running:
    screen.fill(WHITE)
    
    # Håndterer hendelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Håndterer spillerbevegelser
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_velocity
    
    # Tegner spilleren og plattformen
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, BLUE, (platform_x, platform_y, platform_width, platform_height))
    
    # Oppdaterer skjermen
    pygame.display.update()

    # Setter en grense for oppdateringshastighet
    pygame.time.Clock().tick(30)

# Avslutter Pygame
pygame.quit()
sys.exit()
