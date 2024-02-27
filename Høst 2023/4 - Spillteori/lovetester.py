#Oppgave 1

match = 0

navn1 = input("Skriv inn det første navnet")
navn2 = input("Skriv inn det andre navnet")

#Oppgave 2
bosted1 = input("Hvor bor du?")
bosted2 = input("Hvor bor den andre?")


navn1 = navn1.lower()
navn2 = navn2.lower()

første1 = navn1[0]
første2 = navn2[0]

# Hvis navnet har like lange bokstaver så får den 60%

if len(navn1) == len(navn2):
    match = 60
elif første1 == første2:
    match = 40
else:
    match = 15


if bosted1 == bosted2:
    match = match * 1.5


print("Match:", match, "%")
print(f"{navn1} og {navn2} matcher {match}%")














