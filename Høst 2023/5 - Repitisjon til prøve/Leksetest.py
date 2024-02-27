# IT2: Uke 5 - Leksetest 

# Oppgave 1 

# a) Hva bør funksjonen under hete? 
            # høyeste_tall

# b) Kommenter hver linje 

def høyeste_tall (tall_liste):      # definerer tall_liste
    høyeste = tall_liste[0]         # setter høyeste til å være første tallet i listen
    for tall in tall_liste:         # for hvert tall i tall_listen:
        if tall > høyeste:          # hvis tallet er større enn det høyeste:
            høyeste = tall          # bytter ut høyeste med tall
    return høyeste                  # returnerer det høyeste tallet

liste = [1,2,3,4,-100,4]
print(høyeste_tall(liste))




# Oppgave 2 

# a) Hva gjør koden under? 
        # printer antall komma, puntum eller apostroff i teksten

# b) Kommenter hver linje 

tekst = "International Talk Like a Pirate Day is a parodic holiday created in 1995 by John Baur and Mark Summers of Albany, Oregon, who proclaimed September 19 each year as the day when everyone in the world should talk like a pirate. It has since been adopted by the Pastafarianism movement as an official holiday." 
antall = 0                                  # setter antall lik 0:
for bokstav in tekst:                       # for hver bokstav i tekst:
    if bokstav in [",", ".", "'"]:          # h
        antall += 1                         # 
print(antall)                               # printer antall bokstaver i teksten








# Oppgave 3 

# a) Hva gjør kode 1? 
        # hvis du skriver Æ, Ø eller Å vil programmet be om at du skriver det inn på nytt, tar ikke inn de bokstavene

# b) Hva gjør break?
        # break hopper ut av en løkke - printer teksten 

# c) Hva er forskjellen på kode 1 og kode 2? 
        # Kode 1 tar ikke inn de tre bokstavene, kode 2 tar inn de tre bokstavene og returnerer teksten du har skrevet uansett

# d) Hva gjør return?
        # resturnerer det du har puttet inn/veriden



## Kode 1 

while True: 

    tekst = input("Skriv en tekst: ") 

    if not ("Æ" in tekst.upper() or "Ø" in tekst.upper() or "Å" in tekst.upper()):      # hvis ikke æ, ø eller å er i store bokstaver,

        break       # hopper ut av løkken, stopper løkken

print(tekst) 



## Kode 2 

def hent_ASCII_string(spørsmål):        # aski string er en string uten æ,ø,å (amerikansk koding)

    while True: 

        tekst = input(spørsmål) 

        if not ("Æ" in tekst.upper() or "Ø" in tekst.upper() or "Å" in tekst.upper()): 

            return tekst            # gir tilbake tekst men bryter teksten

         

tekst = hent_ASCII_string("Skriv en tekst: ")         # kjører aksi strings

print(tekst) 