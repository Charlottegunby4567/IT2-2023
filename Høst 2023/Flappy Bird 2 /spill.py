import pygame
from fugl import Fugl
from rør import Rør

class Spill:
    def __init__(self):
        self.fugl = Fugl(50, 300)
        self.rører = [Rør(800 + i * 300) for i in range(3)]  # Tre rørsett med mellomrom på 300 piksler
        self.poeng = 0

    def start(self):
        pygame.init()
        VINDU_BREDDE, VINDU_HØYDE = 800, 600
        vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HØYDE))
        pygame.display.set_caption("Flappy Bird")

        klokke = pygame.time.Clock()
        kjører = True

        while kjører:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    kjører = False

            tast = pygame.key.get_pressed()
            self.fugl.oppdater(tast)

            for rør in self.rører:
                rør.oppdater()

                if self.fugl.kollisjon(rør):
                    print("Spillet er slutt! Poeng:", self.poeng)
                    kjører = False

                if self.fugl.passerer_mellomrom(rør) and not rør.passert:
                    self.poeng += 1
                    rør.passert = True

                if rør.x + 50 < self.fugl.x and rør.passert:
                    rør.passert = False

            if self.rører[0].x < -50:
                self.rører.pop(0)
                nytt_rør = Rør(self.rører[-1].x + 300)
                self.rører.append(nytt_rør)

            vindu.fill((173, 216, 230))  # Light Blue
            self.fugl.tegn(vindu)
            for rør in self.rører:
                rør.tegn(vindu, VINDU_HØYDE)  # Pass på å inkludere VINDU_HØYDE her

            font = pygame.font.Font(None, 36)
            tekst = font.render(f'Poeng: {self.poeng}', True, (255, 255, 255))  # Hvitt
            vindu.blit(tekst, (10, 10))
            pygame.display.update()

            pygame.time.delay(30)
            klokke.tick(30)

        pygame.quit()

if __name__ == "__main__":
    nytt_spill = Spill()
    nytt_spill.start()

