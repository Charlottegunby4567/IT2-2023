# Oppgave 3 Med hjelpemidler


# 3.1
    # Lag en funksjon lag_brukernavn som tar inn et fullt navn (f.eks. “Jo Brochmann”) 
    # og returnerer et brukernavn. Brukernavnet skal bestå av personens fornavn, etterfulgt 
    # av den første bokstaven i etternavnet. Alle bokstavene skal være små bokstaver. 
    # For eksempel skal lag_brukernavn("Jo Brochmann") returnere "job".
    # Du kan anta at alle navn kun består av en fornavn og et etternavn.

# LØSNING:
def lag_brukernavn(navn):
    smaa = navn.lower()
    fullt_navn = smaa.split()
    return fullt_navn[0] + fullt_navn[1][0]




# 3.2
    # Lag en funksjon lag_epost som tar inn et navn og en skole som argumenter, og returnerer 
    # en passende epost. Epost-adressen skal bestå av brukernavnet 
    # (samme regler som i 3.1), en @, skolenavnet ogtilslutt.viken.no.
    # For eksempel skal lag_epost("Thor Coward", "Sandvika")returnere thorc@sandvika.viken.no.

# LØSNING:
def lag_epost(navn, skole):
    brukernavn = lag_brukernavn(navn) # bruker funksjonen fra oppgave 3.1 for å generere brukernavn
    skole_smaa = skole.lower()
    return brukernavn + "@" + skole_smaa + ".viken.no"




# 3.3
    # Lag en funksjon fjern_falske_brukere som tar inn en liste med brukernavn og et nøkkelord, 
    # og returnerer en liste med brukernavn som ikke inneholder nøkkelordet. For eksempel skal f
    # jern_falske_brukere(["thorc", "ravim", "ceiliet", "fredrikg"], "fredrik") returnere["thorc", "ravim", "ceciliet"]

# LØSNING:
def fjern_falske_brukere(brukerliste, nokkelord): 
    ekte_brukere = []
    for bruker in brukerliste:
        if nokkelord not in bruker:
            ekte_brukere.append(bruker) 
    return ekte_brukere






# Oppgave 4 med hjelpemidler

# 4.2
    # Skriv klassen Spiller i filen spiller.py med følgende grensesnitt.
    # Klassen skal ha en konstruktør med parameter for navn (i tillegg til self). Konstruktøren skal opprette instansvariablene 
    # _navn, som får verdi fra parameteren navn, og _antall_kamper som skal settes til heltallet 0. I tillegg til konstruktøren 
    # skal klassen ha følgende metoder:
        # hent_navnsomreturnerer_navn
        # hent_antall_kampersomreturnerer_antall_kamper
        # spill_kampsomøker_antall_kampermed1
        # sjekk_navn som tar inn et navn som parameter, og returnerer True hvis spillerens navn in- neholder ett av navnene.
    # For eksempel for spillernavnet “Caroline Graham Hansen” skal sjekk_navn("Caroline" ), sjekk_navn("Hansen") og sjekk_navn
    # ("Caroline Jenssen") alle returnere True, mens sjekk_navn("Karoline") skal returnere False.

# LØSNING:
class Spiller:
    def __init__(self, navn):
        self._navn = navn
        self._antall_kamper = 0

    def hent_navn(self): 
        return self._navn
    def hent_antall_kamper(self): 
        return self._antall_kamper

    def spill_kamp(self):
        self._antall_kamper += 1
    def sjekk_navn(self, navn):
        navneliste_spiller = self._navn.split(" ")
        navneliste_søk = navn.split(" ")

        for navn_søk in navneliste_søk:
            if navn_søk in navneliste_spiller:
                return True 
        return False
    




# 4.2
    # Skriv klassen Lag i filen lag.py med følgende grensesnitt.
    # Klassen skal ha en konstruktør med parameter for navn (i tillegg til self). 
    # Konstruktøren skal opprette instansvariablene _navn, som får verdi fra parameteren navn, 
    # _spillere som er en tom liste, _seier som skal settes til heltallet 0, _uavgjort som skal 
    # settes til heltallet 0 og _tap som skal settes til heltallet 0. I tillegg til konstruktøren 
    # skal klassen ha følgende metoder:
        # hent_navnsomreturnerer_navn
        # hent_poengsomreturnererantallpoenglagethar,hverseiergir3poeng,uavgjortgir1poeng
        # og tap gir 0 poeng.
    # For eksempel skal hent_poeng() returnere 4 for et lag med 1 seier, 1 uavgjort og 2 tap.
        # legg_til_spillersomtarinnenspillersomparameterogleggerdentililisten_spillere • 
        # spill_kampsomøkerantallkamperforallespillernepålagetmed1
        # seiersomøker_seiermed1ogkjørermetodenspill_kamp(slik:self.spill_kamp())
        # uavgjortsomøker_uavgjortmed1ogkjørermetodenspill_kamp
        # tapsomøker_tapmed1ogkjørermetodenspill_kamp
        # finn_spillersomtarinnetnavnsomparameter,hvisenspillerpålagetharnavnetinavnet sitt, returnerer den spilleren, ellers returnerer den None (Samme regler gjelder for sjekk av navn som i metoden sjekk_navn i klassen Spiller).

# LØSNING:
class Lag:
    def __init__(self, navn):
        self._navn = navn
        self._spillere = []
        self._seier = 0
        self._uavgjort = 0
        self._tap = 0 
    
    def hent_navn(self):
        return self._navn 
    
    def hent_poeng(self):
        return self._seier * 3 + self._uavgjort 
    
    def legg_til_spiller(self, spiller):
        self._spillere.append(spiller) 
        
    def spill_kamp(self):
        for spiller in self._spillere: 
            spiller.spill_kamp()

    def seier(self):
        self._seier += 1 
        self.spill_kamp()

    def uavgjort(self): 
        self._uavgjort += 1 
        self.spill_kamp()

    def tap(self):
        self._tap += 1
        self.spill_kamp()

    def finn_spiller(self, spillernavn): 
        for spiller in self._spillere:
            if spiller.sjekk_navn(spillernavn): 
                return spiller
        return None
    




# Oppgave 4.4

# Skriv klassen Serie i filen serie.py med følgende grensesnitt.
# Klassen skal ha en konstruktør med parameter for navn (i tillegg til self). 
# Konstruktøren skal opprette instansvariablene _navn, som får verdi fra parameteren navn 
# og _lag som er en tom liste. I tillegg til konstruktøren skal klassen ha følgende metoder:
        # hent_navnsomreturnerer_navn
        # hent_laglistesomreturnerer_lag.
        # legg_til_lagsomtarinnetlagsomparameterogleggerdentililisten_lag
        # spill_kampsomtarinnparameternehjemmelagsomeretlag-objekt,bortelagsomeret
# lag-objekt, hjemmemaal som er et heltall og bortemaal som er et heltall, hvis et lag har 
# flere mål enn det andre, skal laget med flest mål vinne og det andre laget tape, hvis lagene 
# har like mange mål, skal begge lagene spille uavgjort.
        # finn_spillersomtarinnetnavnsomparameter,hvisenspilleriserienharnavnetinavnet sitt, 
        # returnerer den spilleren, ellers returnerer den None (Samme regler gjelder for sjekk av 
        # navn som i metoden sjekk_navn i klassen Spiller).

# LØSNING:
class Serie:
    def __init__(self, navn): 
        self._navn = navn 
        self._lag = []

    def hent_navn(self): 
        return self._navn
    
    def hent_lagliste(self): 
        return self._lag

    def legg_til_lag(self, lag): 
        self._lag.append(lag)

    def spill_kamp(self, hjemmelag, bortelag, hjemmemaal, bortemaal): 
        if hjemmemaal > bortemaal:
            hjemmelag.seier()
            bortelag.tap()
        elif bortemaal > hjemmemaal:
            hjemmelag.tap()
            bortelag.seier() 
        else:
            hjemmelag.uavgjort()
            bortelag.uavgjort()

    def finn_spiller(self, navn):
        for lag in self._lag:
            spiller = lag.finn_spiller(navn) 
            if spiller:
                return spiller 
        return None