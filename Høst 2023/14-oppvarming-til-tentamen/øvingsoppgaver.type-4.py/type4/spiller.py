class Spiller():
    def __init__(self, navn: str) -> None:
        self.antall_kamper = 0
        self.navn = navn

    def spill_kamp(self):
        self.antall_kamper += 1

    def hent_navn(self):
        return self.navn
    
    def hent_kamper(self):
        return self.antall_kamper
    
    def sjekk_navn(self,navn: str):
        # returner True hvis spileren navn innholder enten Caroline, Graham og Hansen
        
        return navn in self.navn    # /
                                    # /
       # if navn in self.navn:      # / betyr det samme, if-setningen og return
            # return True           # /
        # else:                     # /
            # return False          # /
