# Oppgave 2.3 - Brus

# Skriv et program som ber brukeren om å svare “ja” eller “nei” 
# på om de kunne tenke seg en brus. 

# a) Hvis brukeren har svart “ja” skal programmet skrive ut “Sweet! Her har du en brus.”
# b) Hvis brukeren har svart “nei” skal setningen “Den er grei.” skrives ut.
# c) Hvis brukeren har svart noe annet skal programmet skrive ut “Hæ?”


valg = input("Vil du ha en brus?")
if valg == "Ja":
    print("Her har du en brus.")
elif valg == "Nei":
    print("OK")
else:
    print("Hæ, ja eller nei?")




