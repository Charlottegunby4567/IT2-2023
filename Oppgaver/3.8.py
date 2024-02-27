
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
