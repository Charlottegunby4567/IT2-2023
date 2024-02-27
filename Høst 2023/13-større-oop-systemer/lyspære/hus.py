from rom import Rom

# Oppgave
# a. Lag en hus klasse som inneholder rom, hvert rom inneholder en pære
# b. Lag en metode legg_til_rom som legger til rom i huset
# c. Lag en metode: skru_av_strøm som skrur av alle lys i hele huset
# d. Test huset ditt!!


# a)
class Hus:
    def __init__(self) -> None:
        self._rom: list[Rom] = []

# b)
    def legg_til_rom(self,rom: Rom):
        self._rom.append(rom)

# c)
    def skru_av_strøm (self):
        for rom in self._rom:
            rom.skru_av_lys()

# d)
if __name__=="__main__":
    charlottes_hus = Hus()
    charlottes_hus.legg_til_rom(Rom())