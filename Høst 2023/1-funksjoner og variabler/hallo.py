navn = input("Hva heter du?") # navn er variablen
print("Hallo, "+navn) # kommer som vanlig mellomrom, må lage selv
print("Hallo,", navn) # kommer mellomrom av seg selv
print() # alle ord mellom komma sendes inn som argumenter

print ("Hallo, ",navn,"Heisann", "Hallo", sep="???")



# Oppgave: lag et program som spør om to navn?
# Skriv "Hallo, navn1 og navn2"

navn1 = input ("Person nummer1 hva heter du?")
navn2 = input ("Person nummer2 hva heter du?")
alder1 = ("Hvor gammel er person nummer1?")
alder2 = ("Hvor gammel er person nummer2?")

print(navn1, "er", alder1, "gammel", "og", navn2, "er", alder2, "gammel")