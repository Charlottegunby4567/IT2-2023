def main():

    navn = input ("Hva heter du?")
    skole = input ("Hvilken skole tilhører du?")
    epost = lag_epost (navn, skole)
    print(epost)


def lag_epost(fult_navn, min_skole):
   skole = min_skole.lower
   navn = fult_navn.lower()
   fornavn, etternavn = navn.split()
   return fornavn + etternavn[0] + "@" + skole + ".viken.no"
    
   


main()