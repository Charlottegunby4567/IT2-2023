setning = " ha det fint"
vokaler = ["a","e", "i", "o", "u"]

kopi = ""
for bokstav in setning:
    if bokstav not in vokaler:
        kopi += bokstav
    
print(kopi)