# Oppgave 2


# 2.1
class Bil:
    def __init__(self, merke, modell): 
        self.merke = merke
        self.modell = modell
        self.km = 0

    def kjor(self, antall): 
        self.km += antall

    def hent_km(self): 
        return self.km
    
thors_bil = Bil("Toyota", "Corolla") 
thors_bil.kjor(500) 
print(thors_bil.hent_km())

# det printes ut 500



# 2.2
class Bil:
    def __init__(self, merke, modell):
        self.merke = merke
        self.modell = modell
        self.km = 0


    def kjor(self, antall): 
        self.km += antall
    def hent_km(self): 
        return self.km

thors_bil = Bil("Toyota", "Corolla")
thors_bil.kjor(500)
ravis_bil = Bil("Hyundai", "Ioniq 5")
thors_bil = ravis_bil
thors_bil.kjor(200)
ravis_bil.kjor(100)
print(thors_bil.hent_km())

# det printes ut 300

