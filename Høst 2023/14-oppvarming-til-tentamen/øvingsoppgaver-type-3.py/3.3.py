def fjern_utsolgte (handleliste: list[str], utsolgte: list(str)):
    # Returnere en ny liste som inneholder varene i handleiste
    # Bortsett fra de som også er i utsolgte
    ny_liste = []
    for vare in handleliste:
        if vare in utsolgte:
            ny_liste.append(vare)
    return ny_liste

print (fjern_utsolgte (["melk", "brus", "pasta"], ["kanel", "brus"]))


def fjern_utsolgte (handleliste, utsolgte):
    # Returnere en ny liste som inneholder varene i handleiste
    # Bortsett fra de som også er i utsolgte
    ny_liste = []
    for vare in handleliste:
        if vare in utsolgte:
            print(vare)
            handleliste.remove(vare)
    return handleliste
print (fjern_utsolgte (["melk", "brus", "pasta"], ["kanel", "brus"]))
