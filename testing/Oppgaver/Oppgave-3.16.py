# PRINT "Skriv inn poengsummen din:"

# READ poengsum
# IF poengsum LESSER THAN 50
    # PRINT "Ikkje bestått"  
# ELSE IF poengsum GREATER THAN 50 AND poengsum LESSER THAN 69
    # PRINT "Bestått"     
# ELSE IF poengsum GREATER THAN 70 AND poengsum LESSER THAN 89
    # PRINT "Godt bestått"      
# ELSE IF poengsum GREATER THAN 90 AND poengsum LESSER THAN 100
    # PRINT "Mykje godt bestått"         
# ELSE
    # PRINT "Ikkje gyldig poengsum!"
# ENDIF

print("Skriv inn poengsummen din")
poengsum = int(input(">"))
if poengsum < 50 and poengsum >= 0:
    print("Ikke bestått!")
elif poengsum >= 50 and poengsum <= 69:
    print("Bestått")
elif poengsum >= 70 and poengsum <= 89:
    print("Godt bestått")
elif poengsum >= 90 and poengsum <= 100:
    print("Mykje bestått")
else:
    print("Ikkje gyldig poengsum!")

# Grensepoengsummene mangler, de må inkluderes. Får derfor ikke med oppgitte tall fra oppgaven som en del av poengsummene
# Negative poengsummener må også gi ikke gyldig poengsum