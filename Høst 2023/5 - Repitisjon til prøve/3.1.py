def main():
    navn = input ("Hva heter du?")
    brukernavn = lag_brukernavn(navn)
    print(brukernavn)


def lag_brukernavn(fullt_navn):
    navn = fullt_navn.lower()
    fornavn,etternavn = navn.split()
    return fornavn[0:2] + etternavn[0]      # etter null og under 2

main()




