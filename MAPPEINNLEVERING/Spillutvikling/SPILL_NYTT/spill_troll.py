import pygame  # Importerer pygame-biblioteket for å lage spill
import random  # Importerer random for å generere tilfeldige tall
import sys  # Importerer sys for å bruke systemspesifikke funksjoner som sys.exit()

# Definerer farger som RGB-verdier
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Konfigurerer spillinnstillinger
SCREEN_WIDTH = 600  # Skjermbredde i piksler
SCREEN_HEIGHT = 400  # Skjermhøyde i piksler
BLOCK_SIZE = 40  # Størrelsen på troll og matblokker
SPEED = 3  # Hastigheten som troll beveger seg med

class Troll:
    def __init__(self, x, y):
        self.x = x  # Startposisjon x for troll
        self.y = y  # Startposisjon y for troll
        self.direction = 'RIGHT'  # Starter med å bevege seg mot høyre

    def move(self):
        if self.direction == 'UP':  # Hvis retningen er opp, flytt opp
            self.y -= SPEED
        elif self.direction == 'DOWN':  # Hvis retningen er ned, flytt ned
            self.y += SPEED
        elif self.direction == 'LEFT':  # Hvis retningen er venstre, flytt til venstre
            self.x -= SPEED
        elif self.direction == 'RIGHT':  # Hvis retningen er høyre, flytt til høyre
            self.x += SPEED

class Game:
    def __init__(self):
        pygame.init()  # Initialiserer alle importerte pygame-moduler
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Setter opp skjermstørrelse
        pygame.display.set_caption('Trolljakt')  # Setter tittelen på spillvinduet
        self.clock = pygame.time.Clock()  # Oppretter et klokkeobjekt for å kontrollere oppdateringsrater
        self.troll = Troll(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Oppretter et troll i midten av skjermen
        self.matobjekter = self.generate_food(5)  # Genererer 3 matobjekter tilfeldig plassert
        self.score = 0  # Starter scoren på 0

    def generate_food(self, num_food):
        food = []
        for _ in range(num_food):  # Gjentar for antall matstykker
            food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)  # Tilfeldig x-posisjon på maten
            food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)  # Tilfeldig y-posisjon på maten
            food.append((food_x, food_y))  # Legger til matposisjonen i listen
        return food  # Returnerer listen med matposisjoner

    def draw_objects(self):
        self.screen.fill(BLACK)  # Fyller skjermen med svart
        pygame.draw.rect(self.screen, GREEN, (self.troll.x, self.troll.y, BLOCK_SIZE, BLOCK_SIZE))  # Tegner troll
        for food_pos in self.matobjekter:  # Går gjennom hver matposisjon
            pygame.draw.rect(self.screen, RED, (food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))  # Tegner mat
        font = pygame.font.Font(None, 36)  # Setter fontstørrelse
        score_text = font.render(f'Score: {self.score}', True, WHITE)  # Lager en tekst for poengsum
        self.screen.blit(score_text, (10, 10))  # Viser poengsummen på skjermen
        pygame.display.flip()  # Oppdaterer hele skjermen med det som er tegnet

    def run(self):
        running = True  # Spillet kjører så lenge denne er True
        while running:
            for event in pygame.event.get():  # Henter hendelser fra event-køen
                if event.type == pygame.QUIT:  # Hvis spillvinduet lukkes
                    running = False  # Avslutter spillet
                elif event.type == pygame.KEYDOWN:  # Hvis en tast trykkes ned
                    if event.key == pygame.K_UP:  # Hvis pil opp er trykket
                        self.troll.direction = 'UP'
                    elif event.key == pygame.K_DOWN:  # Hvis pil ned er trykket
                        self.troll.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT:  # Hvis pil venstre er trykket
                        self.troll.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT:  # Hvis pil høyre er trykket
                        self.troll.direction = 'RIGHT'

            self.troll.move()  # Flytter trollet basert på retning

            # Sjekker kollisjon med matobjekter
            for food_pos in self.matobjekter:
                if self.troll.x == food_pos[0] and self.troll.y == food_pos[1]:  # Hvis trollet og maten kolliderer
                    self.score += 1  # Øker scoren med 1
                    self.matobjekter.remove(food_pos)  # Fjerner spist mat
                    # Legger til ny mat på en tilfeldig posisjon
                    self.matobjekter.append((random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE),
                                             random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)))

            # Sjekker for kollisjon med vegger eller hindringer
            if self.troll.x < 0 or self.troll.x >= SCREEN_WIDTH or \
                    self.troll.y < 0 or self.troll.y >= SCREEN_HEIGHT:
                running = False  # Avslutter spillet hvis trollet går ut av skjermen

            self.draw_objects()  # Tegner alle objekter på nytt
            self.clock.tick(15)  # Begrenser spillets framerate til 15

        pygame.quit()  # Avslutter pygame
        sys.exit()  # Avslutter programmet

if __name__ == '__main__':
    game = Game()
    game.run()  # Starter spillet
