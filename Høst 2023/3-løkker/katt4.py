while True:
    antall = int(input("Hvor mange katter har du?"))
    if antall > 0:
        break   # hopper ut av løkken
    print("Ugyldig! Prøv igjen!")
   

for _ in range (antall):
    print("Mjau")
