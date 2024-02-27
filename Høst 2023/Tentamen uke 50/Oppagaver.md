---
title: 'IT2 - Tentamen H23'
date: "12.12.23"
---

> **Del 2 - Med hjelpemidler**

## Oppgave 3 - Spotify royalties

> Tips: i python kan vi skrive `3000000` som `3_000_000`, understrek gjør det litt lettere å jobbe med større tall.

Oppgave 3 leveres i filen `oppgave3.py`.

### 3.1 - Penger per stream

Lag en funksjon `per_stream(land)`, som tar inn et land og returnerer et flyttall som angir hvor mye en artist fra det landet tjener per lytting (stream) på spotify.

Oversikt over land og utbetaling per lytting:

```text
Norge                    $0.55 
Sverige                  $0.44
Finland                  $0.44
Danmark                  $0.52
Island                   $0.62
Resten av verden (snitt) $0.24
```

Eksempler:

```python
print(per_stream("Norge"))  # -> 0.55
print(per_stream("Island")) # -> 0.62
print(per_stream("USA"))    # -> 0.24
```

### 3.2 - Penger tjent på Spotify

Lag en funksjon `andel_til_artist(antall_streams)`, som tar inn et heltall som angir hvor mange streams en artist har og returner hvor stor andel av pengene artisten beholder selv, som et flyttall.

Tabellen under viser en oversikt over trinnene for andeler av penger artistene beholder selv:

```text
Trinn 0 fra          0 til    399 999 streams   0 %
Trinn 1 fra  1 400 000 til 29 999 999 streams  40 %
Trinn 2 fra 30 000 000                streams  70 %
```

Eksempler:

```python
print(andel_til_artist(50_000))     # -> 0
print(andel_til_artist(5_000_000))  # -> 0.40
print(andel_til_artist(50_000_000)) # -> 0.70
```

### 3.3 - Penger tjent

Lag en funksjon `penger_tjent(antall_streams, land)` som tar inn antall streams og land, og returnerer hvor mye penger en artist skal tjene (*antall streams* ganger *penger per stream* ganger *andel til artist*).

> For å få maks uttelling på denne oppgaven må funksjonene fra 3.1 og 3.2 brukes.

Eksempler:

```python
print(penger_tjent(5_000_000, "Norge"))    # -> 90000
print(penger_tjent(100_000_000, "Island")) # -> 104000 
```

### 3.4 - Populære artister

Lag en funksjon `populære(artistliste)` som tar inn en liste med lister, der hver liste inne i listen inneholder artistnavn og antall streams, og returnerer en ny liste med artistene som har over `100 000 000` streams.

Eksempel:

```python
artister = [
    ["Taylor Swift",  109_940_000],
    ["The Weeknd",    105_410_000],
    ["Justin Bieber",  83_820_000],
    ["Drake",          81_980_000],
    ["Ariana Grande",  81_800_000]
]
print(populære(artister)) # -> [["Taylor Swift", 109_940_000], ["The Weeknd", 105_410_000]]
```

### 3.5 - Royalties

Lag en funksjon `royalties(artistliste)` som tar inn en liste med lister, der hver liste inne i listen inneholder artistnavn og antall streams, og returnerer en ny liste med lister der hver liste inne i listen inneholder artistnavn og penger tjent på spotify.

Eksempel:

```python
artister = [
    ["Sígur Ros",        "Island", 1_047_010],
    ["Emma Steinbakken", "Norge",  3_459_239]
]
print(royalties(artister)) # -> [['Sígur Ros', 259658], ['Emma Steinbakken', 761032]]
```

## Oppgave 4 - Musikkbiblioteket

I denne oppgaven skal du lage et program som holder oversikt over sanger og spillelister.

### Sanger som kan brukes til testing

```csv
artist; tittel
Evig Ferie; Oslo vet, Pt.2
Evig Ferie; Seint i går
tigerstate; Look In Her Eyes
Fieh; Supergud
Slomosa; There is Nothing New Under the Sun
Bo Milli; Making Friends
```  

### 4.1 - Modell og oppsett

Les gjennom oppgavetesktene i oppgave 4.2 og 4.3, og tegn et UML-diagram med klassene og metodene til programmet.

> Bruk draw.io eller tegn for hånd.

### 4.2 - Klassen Sang

#### Oppgaver

1. Skriv klassen `Sang` i filen `sang.py`. Se grensesnitt under.
2. Opprett en sang og test alle metodene.

#### Grensesnitt - Sang

Klassen skal ha følgende instansvariabler (egenskaper):

- `tittel`, en streng som inneholder sangens tittel. Eks: `"Jackie Down The Line"`
- `artist`, en streng som inneholder sangens artist. Eks: `"Fontaines D.C."`
- `avspillinger`, et heltall som representerer antall avspillinger. I starten skal `avspillinger` være `0`.

Klassen skal ha følgende metoder:

- `spill` som *spiller* en sang. Metoden skal printe at en sang spilles i terminalen og øke `avspillinger` med `1`. Eksempel på print: `"Spiller Fontaines D.C. - Jackie Down The Line"`
- `sjekk_tittel` som tar inn en parameter `tittel` (streng), og returnerer `True` hvis sangens tittel er lik parameteren `tittel`, ellers skal den returnere `False`.
- `sjekk_artist` som tar inn en parameter `artist` (streng), og returnerer `True` hvis sangens artist er lik parameteren `artist`, ellers skal den returnere `False`.
  
> For eksempel for en sang med tittelen `"Stand By Me"` skal `sjekk_navn("Stand By Me")` returnere `True`, mens `sjekk_navn("Champagne Supernova")` og `sjekk_navn("stand by me")` skal begge returnere `False`.
> Samme regler gjelder for `sjekk_artist`.

### 4.3 - Klassen Spilleliste

1. Skriv klassen `Spilleliste` i filen `spilleliste.py`. Se grensesnitt under.
2. Opprett minst en spilleliste og tre sanger, og test alle metodene.

#### Grensesnitt - Spilleliste

Klassen skal ha følgende instansvariabler (egenskaper):

- `navn`, en streng som inneholder spillelistens navn. Eks: `"Norske favoritter"`
- `sanger`, en liste med sanger. Når en ny spilleliste opprettes skal listen være tom.

Klassen skal ha følgende metoder:

- `legg_til_sang` med en parameter `sang` (Sang), som legger sangen til i listen `sanger`.
- `lengde` som returnerer lengden av spillelisten. Eks: `3`.
- `spill_alle` som *spiller* alle sangene i listen `sanger`
- `tittel_i_liste` med en parameter `tittel` (streng), som returnerer `True` hvis en sang i spillisten har tittelen lik parameteren `tittel`, ellers skal den returnere `False`.
- `artistliste` med en parameter `artist` (streng), som returnerer en liste med alle sangene i spillelisten som har artist lik parameteren `artist`.

> Bonus: Hvis du prøver å printe listen som returneres av metoden `artistliste` vil resultatet bli noe som ligner på `[<__main__.Sang object at 0x000002BF52981100>, <__main__.Sang object at 0x000002BF529813A0>]`. For å fikse dette må du legge til en spesiell metode, `__repr(self)__`, i sang-klassen som returnerer en streng, det kan f.eks være strengen `f"{self.artist} - {self.tittel}"`.
