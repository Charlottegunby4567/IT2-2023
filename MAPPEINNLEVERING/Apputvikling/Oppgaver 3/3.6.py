# Legg til dette i hovedprogrammet hvor menyen blir håndtert

if valg == '2':
    print("Oversikt over alle trenere:")
    for index, trener in enumerate(trenere, 1):
        print(f"{index}. {trener}")



if valg == '3':
    navn = input("Skriv inn navnet på den nye treneren: ")
    ny_trener = Trener(navn)
    trenere.append(ny_trener)
    print(f"Treneren {navn} ble lagt til.")


