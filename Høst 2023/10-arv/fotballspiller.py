from figur import Figur

class Fotballspiller(Figur):
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        super().__init__("bilder/haaland.png")
        self.poeng = 0
        self.liv = 10

        # setter spilleren i startposisjonen
        self.ramme.centerx = vindu_bredde / 2
        self.ramme.bottom = vindu_høyde

    def flytt(self, dx: int):
        self.ramme.x += dx