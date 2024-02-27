elever = ["Hermine", "Harry", "Ronny"]

# print Hermine, Harry og ronny i terminalen ved å bruke lista

# metode 1 - uten løkke:
print (elever[0])
print (elever[1])
print (elever[2])


# metode 2 - med løkke:
for elev in elever:
    print(elev)


# metode 3 - med for-løkke og range:
for i in range(len(elever)):
    print (i, elever[i])

    