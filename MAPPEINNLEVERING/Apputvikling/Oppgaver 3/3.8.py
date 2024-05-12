# UML diagram

# -------------------------------------
# Trener
# -------------------------------------
# - navn : string
# - pokemonListe : list
# -------------------------------------
# + leggTilPokemon(pokemon : Pokemon) : void
# + fjernPokemon(pokemon : Pokemon) : void
# + __str__() : string
# -------------------------------------

# Attributter:
# navn: En streng som lagrer trenerens navn.
# pokemonListe: En liste som holder på alle Pokémonene treneren har.
# Metoder:
# leggTilPokemon(pokemon): Metoden for å legge til en Pokémon i trenerens liste.
# fjernPokemon(pokemon): Metoden for å fjerne en Pokémon fra trenerens liste.
# __str__(): Returnerer en strengrepresentasjon av treneren, inkludert navn og antall Pokémoner de har.




class Trener:
    def __init__(self, navn):
        self.navn = navn
        self.pokemonliste = []

    def legg_til_pokemon(self, pokemon):
        self.pokemonliste.append(pokemon)

    def fjern_pokemon(self, pokemon):
        if pokemon in self.pokemonliste:
            self.pokemonliste.remove(pokemon)
        else:
            print(f"{pokemon} er ikke i pokemonlisten til {self.navn}.")

    def __str__(self):
        antall_pokemon = len(self.pokemonliste)
        return f"Trener {self.navn} har {antall_pokemon} pokemon."


# Eksempel på bruk:
if __name__ == "__main__":
    ash = Trener("Ash")

    print(ash)  # Skriver ut: Trener Ash har 0 pokemon.

    ash.legg_til_pokemon("Pikachu")
    ash.legg_til_pokemon("Charmander")

    print(ash)  # Skriver ut: Trener Ash har 2 pokemon.

    ash.fjern_pokemon("Pikachu")

    print(ash)  # Skriver ut: Trener Ash har 1 pokemon.


# __init__-metoden: Setter opp en ny Trener med et gitt navn og en tom liste for å holde på Pokémoner.
# leggTilPokemon-metoden: Legger til en gitt Pokemon i trenerens liste og rapporterer handlingen.
# fjernPokemon-metoden: Fjerner en Pokemon fra listen hvis den eksisterer, og rapporterer handlingen.
# __str__-metoden: Gir en strengrepresentasjon som viser trenerens navn og antall Pokémon de har.