# Et program som finner fødselsår basert på alder


år = 2024

try:
    alder = int(input("Hvor gammel blir du i år?"))
    fødselsår = år - alder
    print(f"Du er født i {fødselsår}")
except:
    print("Ugyldig input. Input må være et tall")

print("Koden fortsetter...")



# Et annet eksempel
try:
    tall = int(input("Skiv et tall:"))
except:
    print("Ugyldig input. Setter 'tall' til 10")
    tall = 10

print(tall)     # tall er 10 hvis brukeren ikek skriver et tall