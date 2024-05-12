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
            print("Treneroversikt funksjonalitet ikke implementert.")
        elif valg == '3':
            legg_til_trener()
        elif valg == '4':
            print("Avslutter programmet...")
            break
        else:
            print("Ugyldig valg, prøv igjen.")

if __name__ == "__main__":
    main_menu()



# Trener-klassen: Den har blitt enklere og mer fokusert på å håndtere en trener med et navn og en liste over Pokémon.
# trenere-liste: Holder på alle trenerne som er opprettet i systemet.
# legg_til_trener-funksjonen: Spør brukeren om et navn for den nye treneren, oppretter en Trener-instans, og legger denne til i listen over trenere. Denne funksjonen bekrefter også at en ny trener er opprettet.
# main_menu-funksjonen: Hovedmenyen som styrer brukerens valg og utfører funksjoner basert på brukerinput.