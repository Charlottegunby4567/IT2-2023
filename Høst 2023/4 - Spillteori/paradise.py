# Simulering av troskapstesten i Paradise Hotell

def main():
    pott = 0
    print("velkommen til Troskapstesten")
    for i in range(10):
        pott = pott + 10000
        print(f"Runde {i + 1}: {pott}, -")
        if snill_spiller (pott) == False:
            print("Snill spille kastet kula")
            break
        elif slem_spiller (pott) == False:
            print("Slem spiller kastet kula")
            break


def snill_spiller(beløp):
    return True     # beholder kula

# Oppgave 2: lag slem spiller
def slem_spiller(beløp):
    return False # kaster kula


# Oppgave 3: lag en spiller som kaster kula på 30000
def halvveis_spiller(beløp):
    if beløp >= 50000:
        return False
    else:
        return True # spiller kula







main()