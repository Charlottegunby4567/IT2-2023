def main():
    antall = hent_nummer()
    print_mjau(antall)


def hent_nummer():
    while True:
        antall = int(input("Skriv et positivt tall: "))
        if antall > 0:
            return antall #gir tilbake et antall
        print("Ugyldig tall!")


def print_mjau(antall):
    print("Mjau\n" * antall, end="")


main()      #kjører programmet

# en funksjun som henter opp et tall og printer. 