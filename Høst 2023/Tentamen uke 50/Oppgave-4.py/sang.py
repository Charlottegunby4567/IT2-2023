import pygame

class Sang:
    def __init__(self, tittel, artist):
        self.tittel = tittel
        self.artist = artist
        self.avspillinger = 0

    def spill(self):
        print(f"Spiller {self.artist} - {self.tittel}")
        self.avspillinger += 1

    def sjekk_tittel(self, tittel):
        return self.tittel.lower() == tittel.lower()

    def sjekk_artist(self, artist):
        return self.artist.lower() == artist.lower()

if __name__ == "__main__":
    sang1 = Sang("Look In Her Eyes", "Tigerstate")

    sang1.spill()

    print(sang1.sjekk_tittel("Look In Her Eyes")) 
    print(sang1.sjekk_tittel("Making Friends"))  

    print(sang1.sjekk_artist("Evig Ferie"))  
    print(sang1.sjekk_artist("Tigerstate"))    
