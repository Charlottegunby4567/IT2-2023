class Pokemon:
    def __init__(self, navn, nivå, helse, type, angrepListe):
        self.navn = navn
        self.nivå = nivå
        self.helse = helse
        self.type = type
        self.angrepListe = angrepListe

    def __str__(self):
        return f"{self.navn} (HP: {self.helse}, Nivå: {self.nivå})"

# Opprett en tom liste for å holde Pokemon-objekter
pokemon_liste = []

# Definer noen Pokemon-data
pokemon_data = [
    {'navn': 'Pikachu', 'nivå': 5, 'helse': 35, 'type': 'Elektrisk', 'angrepListe': [{'navn': 'Tordenstøt', 'styrke': 40}]},
    {'navn': 'Charmander', 'nivå': 5, 'helse': 39, 'type': 'Ild', 'angrepListe': [{'navn': 'Flamme', 'styrke': 45}]},
    {'navn': 'Squirtle', 'nivå': 5, 'helse': 44, 'type': 'Vann', 'angrepListe': [{'navn': 'Vannstråle', 'styrke': 40}]},
    {'navn': 'Bulbasaur', 'nivå': 5, 'helse': 45, 'type': 'Gress', 'angrepListe': [{'navn': 'Vinstrål', 'styrke': 40}]}
]

# Legg til Pokemon-objekter i listen basert på definerte data
for pd in pokemon_data:
    pokemon = Pokemon(pd['navn'], pd['nivå'], pd['helse'], pd['type'], pd['angrepListe'])
    pokemon_liste.append(pokemon)

# Print ut Pokemon-listen for å bekrefte innholdet
for p in pokemon_liste:
    print(p)



# Vi har definert en klasse Pokemon med en tilpasset __str__-metode for å gi en pen utskrift.
# Vi har opprettet en liste pokemon_liste for å holde Pokemon-objekter.
# Vi har definert en liste av ordbøker pokemon_data som inneholder dataene for hver Pokémon.
# Vi går gjennom pokemon_data med en løkke for å opprette Pokemon-objekter fra dataene og legger dem til i listen pokemon_liste.
# Til slutt, skriver vi ut hver Pokemon i listen for å demonstrere at de har blitt lagt til korrekt.


