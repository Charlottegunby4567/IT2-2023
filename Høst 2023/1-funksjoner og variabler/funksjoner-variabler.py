# Innebygde funksjoner
print("Hei på deg!") # en innebygd funksjon som printer hei på deg i terminalen
input("Hva heter du?") # en innebygd funksjon som printer argumentet (Hva heter du?), lar brukeren skrive inn noe og returnerer det brukeren skriver


# Argumenter
print("Hei på deg!") #f unksjoner kan ta imot argumenter, de skrives mellom parenstesene
print("Hallo", "thor") # noen funksjoner kan ta imot flere argumenter, da skiller vi argumentene med komma
print("hei","verden", end="", sep="!") # end og sep er i dette tilfelle et navngitt argument (named argument)
print ("verden")

# Metoder
## Metoder er funksjoner som hører til "ting", eksmepel metoder som hører til string
navn = "Charlotte Borthen Gunby"
fornavn, mellomnavn, etternavn = navn.split (" ") # split er en metode som splitter en string på argumentet

# Strings (tekst)
## Strings skrives mellom anførselstegn , enten enkle ``eller dobble " "



# Egne funksjoner

def si_hei(til): # definerer en egen funksjon som navn si_hei som tar inn en parameter med navn til
    print("Hei", til) #parameteret til blir til et argument

def spør_om_navn():
    return input ("Hva heter du?") # denne funksjonen returnerer en string



# parameter vs argument!

# parameter er en variabler inne i funksjonen (inne i parentesen)
# argument er 