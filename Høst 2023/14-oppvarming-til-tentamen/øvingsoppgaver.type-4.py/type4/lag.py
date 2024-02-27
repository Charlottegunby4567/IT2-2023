from spiller import Spiller
class Lag:
    def __init__(self, navn):
        self.navn = navn
        self.spillere = []
        self.seier = 0
        self.uavgjort = 0
        self.tap = 0

    def hent_navn(self):
        return self.navn

    def hent_poeng(self):
        return self.seier * 3 + self.uavgjort

    def legg_til_spiller(self, spiller):
        self.spillere.append(spiller)

    def spill_kamp(self):
        for spiller in self.spillere:
            spiller.øk_antall_kamper()

    def seier(self):
        self.seier += 1
        self.spill_kamp()

    def uavgjort(self):
        self.uavgjort += 1
        self.spill_kamp()

    def tap(self):
        self.tap += 1
        self.spill_kamp()

    def finn_spiller(self, navn):
        for spiller in self.spillere:
            if spiller.sjekk_navn(navn):
                return spiller
        return None
