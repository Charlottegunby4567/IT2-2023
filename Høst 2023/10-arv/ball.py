import random
from figur import Figur

class Ball(Figur):
    def __init__(self, vindu_bredde: int) -> None:
        super().__init__("bilder/ball.png")

        # flytter ballen til startposisjonen
        self.ramme.left = random.randint (0, vindu_bredde- self.ramme.width)
        self.ramme.top = 0

    def fall(self, vindu_høyde: int):
        if self.ramme.top > vindu_høyde:
            self.ramme.y = 0
        self.ramme.y += 1
    
