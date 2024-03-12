# Lag en quiz med ett spørsmål "Hvor er dette" "bilde fra et sted"


# Quiz spørsmål og svar
spørsmål1 = "Hva er hovedstaden i Norge?"
svar1 = "Oslo"

spørsmål2 = "Hva er verdens største hav?"
svar2 = "Stillehavet"

spørsmål3 = "Hva er hovedstaden i Frankrike?"
svar3 = "Paris"


# Funksjon for å stille spørsmål og sjekke svar
def stille_spørsmål(spørsmål, riktig_svar):
    svar_fra_bruker = input(spørsmål + "\nSvar: ")
    if svar_fra_bruker.lower() == riktig_svar.lower():
        print("Korrekt!")
        return 1
    else:
        print("Feil. Riktig svar er:", riktig_svar)
        return 0


# Kjør quiz
poengsum = 0
poengsum += stille_spørsmål(spørsmål1, svar1)
poengsum += stille_spørsmål(spørsmål2, svar2)
poengsum += stille_spørsmål(spørsmål3, svar3)

print("Du fikk totalt", poengsum, "av 3 spørsmål riktig.")
