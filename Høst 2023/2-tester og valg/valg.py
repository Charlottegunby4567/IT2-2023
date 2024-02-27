# Oppagve: lag et program som spør brukeren: "hva er x og hva er y?"
# og lagre veridene i to

x = 50
y = 10

x = int(input("hva er x?"))
y = int(input("Hva er y?"))

if x > y:
    print("x er større enn y")
elif x < y:
    print("x er mindre enn y")
else:
    print("x er lik y")

print("Ferdig")