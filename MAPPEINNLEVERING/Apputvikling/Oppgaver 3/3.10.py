class Trener:
    def __init__(self, navn):
        self.navn = navn
        self.pokemonListe = []

    def __str__(self):
        return f"{self.navn} har {len(self.pokemonListe)} Pokémon(er)."

# Liste over trenere
trenere = []

def legg_til_trener():
    navn = input("Skriv inn navnet på den nye treneren: ")
    ny_trener = Trener(navn)
    trenere.append(ny_trener)
    print(f"Trener {navn} er lagt til i systemet.")

def se_treneroversikt():
    if not trenere:
        print("Det er ingen trenere registrert.")
    else:
        print("Treneroversikt:")
        for trener in trenere:
            print(trener)

def main_menu():
    while True:
        print("\nHovedmeny:")
        print("1. Se pokemonoversikt")
        print("2. Se treneroversikt")
        print("3. Lag trener")
        print("4. Avslutt")

        valg = input("Velg et alternativ (1-4): ")

        if valg == '1':
            print("Pokemonoversikt funksjonalitet ikke implementert.")
        elif valg == '2':
            se_treneroversikt()
        elif valg == '3':
            legg_til_trener()
        elif valg == '4':
            print("Avslutter programmet...")
            break
        else:
            print("Ugyldig valg, prøv igjen.")

if __name__ == "__main__":
    main_menu()


# se_treneroversikt-funksjonen: Denne funksjonen sjekker først om det er noen trenere registrert. Hvis listen trenere er tom, informerer den brukeren om at ingen trenere er registrert. Hvis det finnes trenere, lister den opp hver trener med en beskrivelse av hvor mange Pokémon de har.
# Hovedmenyen: Integrerer den nye funksjonen se_treneroversikt i menyvalg 2. Brukeren kan velge dette alternativet for å se en oversikt over alle trenere.