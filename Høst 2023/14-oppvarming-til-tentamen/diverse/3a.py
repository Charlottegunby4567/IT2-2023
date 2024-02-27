# Program for reisekarantene
    
def karantene(vaksinert, farge):
    if vaksinert:
        return 0

    elif farge == "rød" or farge == "oransje":
        return 10

    elif farge == "grønn":
        return 3
    
print(karantene(True, "rød"))
print(karantene(False, "grønn"))
print(karantene(False, "rød"))
print(karantene(False, "oransje"))

