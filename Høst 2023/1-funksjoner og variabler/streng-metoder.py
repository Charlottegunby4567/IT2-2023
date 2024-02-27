# input er en funksjon som tar inn et argument og returnerer det brukeren skriver inn i terminalen
navn = input ("Hva heter du? (Fornavn og etternavn)")

# Hva er navn?
# Navn er en variabelsom inneholder en string etter vi har kjørt linjen med kode

# split er en streng-metode som spliter en string (tekst)

fornavn, etternavn = navn.split(" ")
fornavn = fornavn.capitalize()
navn = navn.title()



# print Hallo, NAVN i terminalen
print("Hallo,", fornavn)
print("Ditt fulle navn er:", navn)
