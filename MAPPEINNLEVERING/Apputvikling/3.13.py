while True:                                            # Starter en uendelig løkke som kjører til en break-setning er nådd
    try:                                               # Begynner et try-blokk for å prøve å kjøre koden som kan kaste en feil
        alder = int(input("Hvor gammel er du? "))      # Forsøker å konvertere brukerens input til et heltall (int) og lagrer det i variabelen alder
        break                                          # Avslutter løkken dersom konvertering til int var vellykket
    except:                                            # Håndterer eventuelle unntak (feil) som oppstår i try-blokken
        print("Ugyldig input. Alder må være et tall.") # Skriver ut en feilmelding dersom input ikke kan konverteres til int

år = 2024                                              # Setter variabelen år til 2024
fødselsår = år - alder                                 # Beregner fødselsåret ved å trekke den angitte alderen fra året 2024
print(f"Du er født i {fødselsår}")                     # Printer en formatert streng som viser det beregnede fødselsåret
