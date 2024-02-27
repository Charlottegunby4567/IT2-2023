import json
from politiker import Politiker
from fantasiparti import Fantasiparti




with open ("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)


representanter = data ["dagensrepresentanter_liste"]


politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)


print("-- Velkommen til Stortinget-fantasy --")
print()
print("Hva skal partiet hete?")
navn = input (">")
print ("Hva heter eieren av paritet?")
eier = input (">")
spillerparti = Fantasiparti(navn, eier)


print()
print("Et nytt politisk parti er stiftet!")
print("Trykk enter for å starte spillet")
input()


while True:
    # rens_terminal()
    print("-- Stortinget-fantasy --")
    print("1: Vis politikeroversikt")
    print("2: Mitt parti")
    print("3: Kjøp politiker")
    print("4: Avslutt")
    brukervalg = input (">")

    if brukervalg == "1":
        print("-- Politikeroversikt --")
        for politiker in politikere:
            print(politiker)
        print ("Trykk enter for å gå tilbake til hovedmenyen")
        input()

    elif brukervalg == "2":
        # rens_terminal()
        spillerparti.vis_partioversikt()
        print("Trykk enter for å gå tilbake til hovedmenyen")
        input()

    elif brukervalg == "3":
        # rens_terminal
        print("Kjøp politiker")
        print()
        print("Hvem ønsker du å kjøpe? Skriv ID til politiker.")
        politiker.id = input (">")

        for politiker in politikere:
            if politiker.id == politiker.id:
                spillerparti.kjøp_politiker(politiker)
                break
        print("Trykk enter for å gå tilbake til hovedmenyen")
        input()

    elif brukervalg == "9":
        print("Avslutter..")
        break

    else:
        print("Trykk enter for å gå tilbake til hovedmenyen")
        input()

print("Takk for nå")