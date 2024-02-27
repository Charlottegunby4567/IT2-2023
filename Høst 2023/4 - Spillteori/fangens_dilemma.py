# Oppgave 1

def beregn_score(valg_spiller1, valg_spiller2):
    if valg_spiller1 == "samarbeid" and valg_spiller2 == "svik":
        return [5,0]
    
    elif valg_spiller1 == "svik" and valg_spiller2 == "samarbeid":
        return [0,5]
    
    elif valg_spiller1 == "svik" and valg_spiller2 == "svik":
        return [0,0] 

    elif valg_spiller1 == "samarbeid" and valg_spiller2 == "samarbeid":
        return [2,5,2,5]
    
score = beregn_score ("svik", "svik")
print(score)




# Oppgave 2

def spill_snilt (motspiller):        # det som står mellom () er parameter
    antall_samarbeid = motspiller.count("svik")     #teller antall svik i motspiller lista
    antall_svik = motspiller.count("samarbeid")     #teller antall samarbeid i motspiller lista
    if antall_svik > antall_samarbeid:
        return "svik"
    else:
        return "samarbeid"



# Oppgave 3
 # tips: len(motspiller) --> lengden av lista

def slem_spiller (motspiller):
    antall_spill = len(motspiller)  #
    if antall_spill <= 5:           # samarbeide de første 5
        return "samarbeid"
    else:
        return"svik"                # etter 5 spill blir det svik

