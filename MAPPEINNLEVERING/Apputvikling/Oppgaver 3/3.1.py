import json

def main_menu():
    while True:
        print("\nHovedmeny:")
        print("1. Se pokemonoversikt")
        print("2. Se treneroversikt")
        print("3. Lag trener")
        print("4. Avslutt")

        valg = input("Velg et alternativ (1-4): ")

        if valg == '4':
            print("Avslutter programmet...")
            break
        elif valg in ['1', '2', '3']:
            print(f"Du valgte alternativ {valg}.")
        else:
            print("Ugyldig valg, prøv igjen.")

if __name__ == "__main__":
    main_menu()

