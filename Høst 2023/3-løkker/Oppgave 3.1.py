# Hos friske mennesker varierer kroppstemperaturen vanligvis mellom 36.5 og 37.5 grader.
# Lag et program som ber brukeren skrive inn kroppstemperaturen sin, 
# avgjør om kroppstemperaturen ligger henholdsvis under, innenfor eller 
# over normal kroppstemperatur og skriver ut en passende melding.


inp = input("Hva er din kroppstemperatur?")
temp = float(inp)
if temp < 36.5 : 
    print("Du har lavere kroppstemperatur enn normalt")
elif temp > 37.5 :
    print("Du har høyere kroppstemperatur enn normalt")
else:
    print("Du har normal kroppstemperatur")

