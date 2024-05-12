import json

# Funksjon for å lese inn JSON-data fra en fil
def load_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

# Sti til JSON-filen
file_path = 'pokemon.json'

# Lese innholdet av JSON-filen og lagre det i en variabel
pokemon_data = load_json_file(file_path)

# Print ut data for å bekrefte innlesningen
print(pokemon_data)
