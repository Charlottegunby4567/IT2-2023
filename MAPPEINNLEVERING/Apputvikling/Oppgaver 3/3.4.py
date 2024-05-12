class Pokemon:
    def __init__(self, navn, nivå, helse, type, angrepListe):
        self.navn = navn
        self.nivå = nivå
        self.helse = helse
        self.type = type
        self.angrepListe = angrepListe

    def angripe(self, motstander):
        # Implementer funksjonalitet for å velge et angrep og påføre skade
        if not self.angrepListe:
            print(f"{self.navn} har ingen angrep tilgjengelig.")
            return
        
        # Eksempel: bruker det første angrepet i listen
        angrep = self.angrepListe[0]
        skade = angrep['styrke']  # Antar at angrep har en 'styrke'-nøkkel
        print(f"{self.navn} bruker {angrep['navn']} og påfører {skade} skade.")
        motstander.mottaSkade(skade)

    def mottaSkade(self, skade):
        self.helse -= skade
        print(f"{self.navn} mottar {skade} skade, gjenstående helse: {self.helse}")
        if self.helse <= 0:
            print(f"{self.navn} er nedkjempet!")

    def erNedkjempet(self):
        return self.helse <= 0

# Eksempel på hvordan klassen kan brukes
if __name__ == "__main__":
    angrepListe = [{'navn': 'Tordenstøt', 'styrke': 40}]
    pikachu = Pokemon('Pikachu', 5, 35, 'Elektrisk', angrepListe)
    charmander = Pokemon('Charmander', 5, 39, 'Ild', angrepListe)

    pikachu.angripe(charmander)
    if charmander.erNedkjempet():
        print(f"{charmander.navn} er ute av kampen.")


# __init__-metoden: Setter opp en ny Pokémon med de gitt attributtene.
# angripe-metoden: Denne metoden simulerer en angrepsrunde hvor Pokémonen bruker et angrep mot en motstander. Den antar at et angrep inneholder et navn og en styrke. Denne metoden vil trenge videre tilpasning basert på ditt spesifikke spill og angrepslogikk.
# mottaSkade-metoden: Reduserer Pokémonens helse basert på den mottatte skaden og skriver ut den gjenværende helsen. Hvis helsen faller til null eller lavere, bekrefter den at Pokémonen er nedkjempet.
# erNedkjempet-metoden: Returnerer en boolean verdi som indikerer om Pokémonen er nedkjempet, basert på helsen.
