# Lyspære
class Lyspære():
    def __init__(self):
        self._på = False

    def tenn(self):
        self._på = True

    def slukk (self):
        self._på = False

    def er_på (self):
        # returnere true hvis pære er på og false hvis pæra er av
        return self._på



# Linja under sørger for at test-koden kun kjøres når vi trykker play på denne fila
if __name__== "__main__":
    # Test kode
    min_pære = Lyspære()
    stue_pære = Lyspære()

 # Skru på stuepærene!!
    stue_pære.tenn()

# Skru av stuepærene!!
    stue_pære.slukk()

    if stue_pære.er_på:
        print("Pæra i stua er på!!")

# slutt på testkode