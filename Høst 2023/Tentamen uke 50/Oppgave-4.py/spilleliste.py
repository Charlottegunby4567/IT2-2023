import pygame
from sang import Sang

class Spilleliste:
    def __init__(self, navn):
        self.navn = navn
        self.sanger = []

    def legg_til_sang(self, sang):
        self.sanger.append(sang)

    def lengde(self):
        return len(self.sanger)

    def spill_alle(self):
        for sang in self.sanger:
            print(f"Spiller nå: {sang}")

    def tittel_i_liste(self, tittel):
        for sang in self.sanger:
            if sang.tittel == tittel:
                return True
        return False

    def artistliste(self, artist):
        return [sang for sang in self.sanger if sang.artist == artist]


if __name__ == "__main__":
    norske_favoritter = Spilleliste("Norske favoritter")

    sang1 = Sang ("Fieh", "Supergud")
    sang2 = Sang ("Evig Ferie", "Seint i går")
    sang3 = Sang ("Slomosa", "There is Nothing New Under the Sun")

    norske_favoritter.legg_til_sang(sang1)
    norske_favoritter.legg_til_sang(sang2)
    norske_favoritter.legg_til_sang(sang3)

    print(f"Lengden av spillelisten er: {norske_favoritter.lengde()}")
    print(f"Er 'Seint i går' i spillelisten? {norske_favoritter.tittel_i_liste('Seint i går')}")
    
