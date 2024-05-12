class Pokemon:
    def __init__(self, navn, nivå, helse, type, angrepListe):
        self.navn = navn
        self.nivå = nivå
        self.helse = helse
        self.type = type
        self.angrepListe = angrepListe

    def angripe(self, motstander):
        if not self.angrepListe:
            print(f"{self.navn} har ingen angrep tilgjengelig.")
            return
        
        angrep = self.angrepListe[0]
        skade = angrep['styrke']
        print(f"{self.navn} bruker {angrep['navn']} og påfører {skade} skade.")
        motstander.mottaSkade(skade)

    def mottaSkade(self, skade):
        self.helse -= skade
        print(f"{self.navn} mottar {skade} skade, gjenstående helse: {self.helse}")
        if self.helse <= 0:
            print(f"{self.navn} er nedkjempet!")

    def erNedkjempet(self):
        return self.helse <= 0

    def __str__(self):
        return f"{self.navn} (HP: {self.helse}, Nivå: {self.nivå})"

# Eksempel på hvordan klassen kan brukes
if __name__ == "__main__":
    angrepListe = [{'navn': 'Tordenstøt', 'styrke': 40}]
    pikachu = Pokemon('Pikachu', 5, 35, 'Elektrisk', angrepListe)
    charmander = Pokemon('Charmander', 5, 39, 'Ild', angrepListe)

    print(pikachu)  # Skriver ut: Pikachu (HP: 35, Nivå: 5)
    pikachu.angripe(charmander)
    if charmander.erNedkjempet():
        print(f"{charmander.navn} er ute av kampen.")

# __str__-metoden: Denne metoden returnerer en streng som beskriver Pokémonen, inkludert navnet, helsen (HP), og nivået. 
# Denne metoden gjør det lett å få en rask oversikt over tilstanden til en Pokémon når du skriver ut objektet.