

class Person:
    """
        Klasse for en person.

        Parametere:
            fornavn (str): Personens fornavn
            etternavn (str): personens etternavn
            fødselsdato (int): personens fødselsdato på formen YYYY
    """


    def __init__(self, fornavn: str, etternavn: str, fødselsår: int):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = fødselsår

    def beregn_alder(self):
        return 2023 - self.fødselsår
    
    def vis_info(self):
        print(f"{self.fornavn} {self.etternavn} {self.beregn_alder()}")


# Lag tre personer
person1 = Person("Charlotte", "Borthen Gunby", 2005)
person2 = Person("Marielle", "Borthen Gunby", 2008)
person3 = Person("Line", "Borthen Gunby", 1978)
person4 = Person("Ole Kristian", "Gunby", 1977)


class Lærer(Person):
    def __init__(self, fornavn, etternavn, fødselsår, fag):
        super().__init__(fornavn, etternavn, fødselsår)
        self.fag = fag

class Elev(Person):
    def __init__(self, fornavn, etternavn, fødselsår, klassetrinn):
        super(). __init__(fornavn, etternavn, fødselsår)
        self.klassetrinn = klassetrinn

class Rektor(Person):
     def __init__(self, fornavn: str, etternavn: str, fødselsår: int, skole: str):
         super().__init__(fornavn, etternavn, fødselsår)
         self.skole = skole


Eva = Lærer("Eva", "Hey", 1960, "Matte")
Camilla = Elev("Camilla", "Hey", 1999, 3)
Ann_Hege = Rektor("Ann Hege", "Jerve", 1869, "Sandvika VGS")
Ann_Hege.vis_info()