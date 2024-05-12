class Trener:
    def __init__(self, navn):
        self.navn = navn
        self.pokemonListe = []

    def leggTilPokemon(self, pokemon):
        if isinstance(pokemon, Pokemon):
            self.pokemonListe.append(pokemon)
            print(f"{pokemon.navn} er lagt til i {self.navn}s team.")
        else:
            print("Kun gyldige Pokémon-objekter kan legges til.")

    def __str__(self):
        return f"{self.navn} har {len(self.pokemonListe)} Pokémon(er)."

# Sørg for at Pokemon-klassen er definert for å teste dette.
class Pokemon:
    def __init__(self, navn, nivå, helse, type, angrepListe):
        self.navn = navn
        self.nivå = nivå
        self.helse = helse
        self.type = type
        self.angrepListe = angrepListe
    
    def __str__(self):
        return f"{self.navn} (Nivå: {self.nivå}, HP: {self.helse})"

# Eksempel på bruk av Trener-klassen
if __name__ == "__main__":
    ash = Trener("Ash")
    pikachu = Pokemon('Pikachu', 5, 35, 'Elektrisk', [{'navn': 'Tordenstøt', 'styrke': 40}])
    ash.leggTilPokemon(pikachu)
    print(ash)


# leggTilPokemon-metoden: Tar et Pokemon-objekt som parameter og legger det til i pokemonListe. Før tilleggingen verifiseres det at objektet faktisk er en instans av Pokemon-klassen for å sikre integriteten til dataene som lagres.
# __str__-metoden: Returnerer en beskrivelse av treneren som inkluderer antall Pokémon de har.
