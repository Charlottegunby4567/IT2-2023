# Et program som fortsetter helt tiul bruker har skrevet riktig input

år = 2024

while True:
    try:
        alder = int(input("Hvor gammel blir du i år?"))
        break
    except:
        print("Ugyldig input. Input må være et tall")

fødselsår = år - alder
print(f"Du er født i {fødselsår}")


