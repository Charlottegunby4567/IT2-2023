import pygame
from hovedmeny import Hovedmeny

class Vindu():
    def __init__(self) -> None:
        pygame.init()
        self.bredde = 600
        self.høyde = 600
        self.vindu = pygame.display.set_mode((self.bredde, self.høyde))
        self.klokke = pygame.time.Clock()
        self.fps = 60


        self.tilstand = "meny"
        self.meny = Hovedmeny(self.bredde, self.høyde, [
            {
                "tekst": "Spill",
                "handling": self.vis_spill
            },
            {
                "tekst": "Avslutt",
                "handling": self.avslutt
            }
        ])

        
        self.spill = None

    def vis_spill(self):
        self.tilstand = "spill"

    def vis_meny(self):
        self.tilstand = "meny"

    def avslutt(self):
        pygame.quit()
        raise SystemExit
    
    def kjør(self):
        while True:
            # Håndter input
            hendelser = pygame.event.get()
            for hendelse in hendelser:
                if hendelse.type == pygame.QUIT:
                    self.avslutt()
        # trykker jeg på kryss avsluttes spillet automatisk
            
            pygame.display.flip()
            self.klokke.tick(self.fps)

spillvindu = Vindu()
spillvindu.kjør()
