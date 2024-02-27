elever = [
    {"navn": "Hermine", "hus": "Griffing", "patronus": "Oter"},
    {"navn": "Harry", "hus": "Griffing", "patronus": "Hjort"},
    {"navn": "Ronny", "hus": "Griffing", "patronus": "Jack Russell Terrier"},
    {"navn": "Draco", "hus": "Smygard", "patronus": None}
]

# Oppgave: print denne informasjonen ut i terminalen
# Hermine, Griffing, Oter
# ...
# ...
# ...

for elev in elever:
    print(elev["navn"], ":", elev ["hus"], "->", elev["patronus"])