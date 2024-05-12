class Pokemon:
    def __init__(self, navn, nivå, helse, type, angrepListe):
        self.navn = navn
        self.nivå = nivå
        self.helse = helse
        self.type = type
        self.angrepListe = angrepListe

    def __str__(self):
        return f"{self.navn} (HP: {self.helse}, Nivå: {self.nivå}, Type: {self.type})"

# Liste over Pokemon
pokemon_liste = [
    Pokemon('Pikachu', 5, 35, 'Elektrisk', [{'navn': 'Tordenstøt', 'styrke': 40}]),
    Pokemon('Charmander', 5, 39, 'Ild', [{'navn': 'Flamme', 'styrke': 45}]),
    Pokemon('Squirtle', 5, 44, 'Vann', [{'navn': 'Vannstråle', 'styrke': 40}]),
    Pokemon('Bulbasaur', 5, 45, 'Gress', [{'navn': 'Vinstrål', 'styrke': 40}])
]

def se_pokemonoversikt():
    if not pokemon_liste:
        print("Det er ingen Pokémon registrert.")
    else:
        print("Pokémonoversikt:")
        for pokemon in pokemon_liste:
            print(pokemon)

def main_menu():
    while True:
        print("\nHovedmeny:")
        print("1. Se pokemonoversikt")
        print("2. Se treneroversikt")
        print("3. Lag trener")
        print("4. Avslutt")

        valg = input("Velg et alternativ (1-4): ")

        if valg == '1':
            se_pokemonoversikt()
        elif valg == '2':
            print("Treneroversikt funksjonalitet ikke implementert.")
        elif valg == '3':
            print("Lag trener funksjonalitet ikke implementert.")
        elif valg == '4':
            print("Avslutter programmet...")
            break
        else:
            print("Ugyldig valg, prøv igjen.")

if __name__ == "__main__":
    main_menu()

# Pokemon-klasse: Jeg har lagt til en __str__-metode i Pokemon-klassen for å gi en pen utskrift av hver Pokémon som inneholder navn, helse, nivå og type.
# pokemon_liste: En liste som inneholder flere Pokemon-objekter.
# se_pokemonoversikt-funksjon: Denne funksjonen skriver ut en oversikt over alle Pokémonene i listen. Hvis listen er tom, informerer den brukeren om dette.
# main_menu-funksjon: En hovedmeny som lar brukeren velge mellom ulike alternativer, der alternativ 1 nå viser en oversikt over alle Pokémonene.