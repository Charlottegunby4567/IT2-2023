import random

def main():
    print("Velkommen til Troskapstesten")
    spiller1 = 0
    spiller2 =0
    for i in range (100000):
        resultat = spill(usikker, halvveis)
        spiller1 += resultat[0]
        spiller2 += resultat[1]
        print(spiller1, spiller2)


def snill(beløp):
    # en funksjon for en snill stategi, som alltid beholder kula
    return "behold"



def slem(beløp):
    # en funksjon for en slem strategi, som alltid kaster kula
    return "kast"



def halvveis(beløp):
    if beløp >= 150000:
        return "kast"
    else:
        return "behold"
    


def veldig_usikker(beløp):
    # en spiller som kaster kula 50% av gangene

    tilfeldig_tall = random.randint(1,100)
    if tilfeldig_tall <= 50:
        return "behold"
    else:
        return "kast"



def usikker(beløp):
    # en funksjon for en spiller som 30% av gangene kaster når beløpet er under 50000,
    # og kaster kule 70% av gangene når beløpet er 50000 eller mer.
    
    tilfeldig_tall = random.randint(1,100)
    if beløp < 50000:
        if tilfeldig_tall <= 30:
            return "kast"
        else: 
            return "behold"
    else: 
        if tilfeldig_tall <= 70:
            return "kast"
        else:
            return "behold"
        

    


def spill(strategi1, strategi2):
    # en funksjon som spiller troskapstesten fra paradise hotell
    # funksjonen returnerer en liste med gevinsten til hver spiller
    # f.eks. [10000, 0] eller [150000, 150000] eller [og, 800000] og så videre...
    # en liste med gevinst til siller en og en gevinst til spiller to
    # kaster ingen kula får de 150000 hver

    pott = 0                # potten er 0 i starten
    for i in range(30):
        pott += 10000       # øker potten med 10 000
        if strategi1 (pott) == "kast":
            return [pott, 0]
        elif strategi2 (pott) == "kast":
            return [0,pott]
        

    return [pott / 2, pott /2] # ingen kasta kula, spillerne deler potten

main()