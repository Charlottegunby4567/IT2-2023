alder = int(input("Hvor mange prosent rett fikk du på prøven?"))

if prosent >= 93.33:
    print("Karakter: 6")
elif prosent >= 85:
    print("Karakter: 5")
elif prosent >= 65:
    print("Karakter: 4")
elif prosent >= 40:
    print("Karakter: 3")
elif prosent >= 20:
    print("Karakter: 2")
else:
    print("Karakter: 1")



# if-setning påe n linje
x = 12
y = 14

print("x") if x > y else print ("y")

# samme if-setning på vanlig måte:
if x > y:
    print("x")
else:
    print("y")