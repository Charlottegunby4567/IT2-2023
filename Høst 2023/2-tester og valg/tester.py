# intro

logget_inn = False

if logget_inn:
    print("Velkommen!")
else:
    print("Logg inn!!!")


# teste


## Sammenligningsoperatorer
3 > 2  # TRUE. Større enn (den ti vesntre er større enn den til høyre)
3 >= 3 # TRUE. Større eller lik
2 < 3  # TRUE. Større enn
2 <= 2 # TRUE. Mindre eller lik
3 == 3 # TRUE. Lik
2 != 3 # TRUE. Ikke lik

print (3 != 2) # printer True i terminalen
resultat_av_test = 42 == 12
print (resultat_av_test)



# Logiske operatorer
alder = 71
yrke = "lærer"

alder > 70 and yrke == "lærer" # -> True
alder < 70 or yrke == "lærer"  # -> ???
# alder < 70 = false, yre =="lærer"= true : True (på grunn av or)

not alder > 70 # -> False

# and
# or
# not