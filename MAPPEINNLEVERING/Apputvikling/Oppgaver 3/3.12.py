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

    def fjernPokemon(self, pokemon):
        if pokemon in self.pokemonListe:
            self.pokemonListe.remove(pokemon)
            print(f"{pokemon.navn} er fjernet fra {self.navn}s team.")
        else:
            print(f"{pokemon.navn} er ikke i {self.navn}s team.")

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
    ash.fjernPokemon(pikachu)
    print(ash)



# fjernPokemon-metoden: Denne metoden tar inn et Pokemon-objekt som parameter. Hvis Pokémonen finnes i trenerens liste, blir den fjernet, og det printes en melding om at Pokémonen er fjernet. Hvis Pokémonen ikke er i listen, informeres brukeren om dette.
# Metoden sikrer også at bare objekter som faktisk er i listen blir fjernet, noe som hjelper med å vedlikeholde dataintegriteten i applikasjonen.