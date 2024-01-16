# Oppgave 9 - 12 - ALgortimer, pseudokode og flytdiagram


## Oppgave 9

### I figuren nedenfor finner du en illustrasjon som viser et flytskjema for en algoritme, og i kodeboksen under figuren finner du fire sekvenser med pseudokode.

```psudeo
1:
SET n TO 1
WHILE n LESSER THAN OR EQUAL TO 10
  INCREMENT n
  DISPLAY n
ENDWHILE

2:
SET n TO 0
FOR hver n LESSER THAN OR EQUAL TO 10
  DISPLAY n
ENDFOR

3:
SET n TO 1
WHILE n LESSER THAN 10
  DISPLAY n
  INCREMENT n
ENDWHILE

4:
SET n TO 1
FOR hver n LESSER THAN OR EQUAL TO 10
  DISPLAY n
ENDFOR
```

> Hvilken sekvens med pseudokode gir lik visning av output som algoritmen beskrevet av flytskjemaet? Velg riktig svar:

- [] 1
- [x] 2
- [] 3
- [] 4


## Oppgave 10

### Nedenfor finner du flere linjer med pseudokode. Sorter linjene i riktig rekkefølge, slik at det blir pseudokoden til et program som skal finne det største tallet av tre tall. Tips: Linjene med pseudokode har ikke innrykk/indentering.

#### Eksempel på svar:
- G-1
- A-2
- D-3
- ...

> 
    B. SET størst TO første tall
    A. IF andre tall GREATER THAN størst
    C. SET størst TO andre tall
    D. IF tredje tall GREATER THAN størst




## Oppgave 11

> a. Du får i oppgave å finne det nest største tallet i en liste (array) med tall. Dersom det finnes flere like tall som er størst, skal ingen av disse regnes som nest størst. Under finner du fire alternative løsninger for denne oppgaven skrevet i pseudokode. Hvilke to løsninger er riktige?

```psuedo
1. 
SET størst TO negativt uendelig tall
FOR hvert tall i listen
  IF tall GREATER THAN størst
    SET størst TO tall
  ENDIF
ENDFOR
Fjern størst fra listen
SET nestStørst TO negativt uendelig tall
FOR hvert tall i listen
  IF tall GREATER THAN nestStørst 
    SET nestStørst TO tall
  ENDIF
ENDFOR
DISPLAY nestStørst

2.
SET størst TO første tall i listen
SET nestStørst TO andre tall i listen
IF nestStørst GREATER THAN størst
  Bytt størst og nestStørst
ENDIF
FOR hvert tall i listen med start fra tredje tall
  IF tall GREATER THAN størst
    SET nestStørst TO størst
    SET størst TO tall
  ELSEIF tall GREATER THAN nestStørst AND tall NOT EQUAL TO størst
  SET nestStørst TO tall
  ENDIF
ENDFOR
DISPLAY nestStørst

3.
SET størst TO negativt uendelig tall
SET nestStørst TO negativt uendelig tall
FOR hvert tall i listen
  IF tall GREATER THAN størst
    SET nestStørst TO størst
    SET størst TO tall
  ELSEIF tall GREATER THAN nestStørst
    SET nestStørst TO tall
  ENDIF
ENDFOR
DISPLAY nestStørst

4.
Sorter listen i synkende rekkefølge
FOR hvert tall i listen
    IF tall NOT EQUAL TO neste tall i listen
        DISPLAY neste tall i listen
        avbryt for-løkken
    ENDIF
ENDFOR
```

> Velg de to riktige løsningene.

- [] 1
- [x] 2
- [x] 3
- [] 4


> b. Skriv en kort tekst der du vurderer og sammenligner de to løsningene du valgte i punkt a.
    Løsning 2:
        Denne løsningen starter med å sette de to første tallene som størst og nest størst, og deretter går gjennom resten av listen for å oppdatere størst og nest størst. Den håndterer tilfeller der det finnes flere like tall som er størst, og den bytter størst og nest størst hvis nødvendig. Denne tilnærmingen ser ut til å være korrekt og effektiv.

    Løsning 3:
        Denne løsningen bruker en lignende tilnærming som løsning 2, men den oppdaterer nest størst selv om det finnes flere like tall som er størst. Dette kan føre til feil resultat, siden det spesifikke kravet er å ikke regne med flere like tall som størst. Derfor er løsning 3 ikke korrekt for oppgaven.

        Generelt sett er løsning 2 den mest passende, da den tar hensyn til kravet om ikke å inkludere flere like tall som størst, og den håndterer også andre scenarier effektivt.



## Oppgave 12

### Elementene i en indeksert variabel (liste/array) skal sorteres i stigende rekkefølge etter følgende algoritme: Man sammenligner hvert element fra venstre til høyre i listen med neste element, og hvis elementet er større enn neste element, bytter de plass. Deretter går man videre til neste element og sammenligner på nytt frem til hele listen er gjennomgått. Dette gjentas til hele listen gjennomgås uten at det forekommer noen ombyttinger.

### Under finner du deler av pseudokoden for denne algoritmen. Her er a en liste med n elementer, og a[ i ] er elementet på plass i i listen.

```psuedo
SET i TO 0
FOR hver i LESSER THAN n - 1
  IF a[i] GREATER THAN a[i+1]    
    CALL byttPlass()
  ENDIF
ENDFOR
```

> a. Hva blir innholdet i listen etter at vi har kjørt programmet representert ved pseudokoden over for listen a = [8, 5, 2, 6, 12], som har n = 5 elementer? Velg riktig svar.

- [] [ 5, 8, 2, 6, 12 ]
- [] [ 5, 2, 8, 6, 12 ]
- [x] [ 5, 2, 6, 8, 12 ]
- [] [ 2, 5, 6, 8, 12 ]


> b. Utvid pseudokoden slik at programmet den representerer, sorterer ferdig listen a i stigende rekkefølge etter altgoritmen som er vist øverst. Forklar endringene du gjør. Obs! Du må også lage pseudokode for funksjonen byttPlass().

```psuedo
SET i TO 0
SET byttet TO true  // Ny variabel for å spore om det ble gjort bytter
WHILE byttet IS true  // Fortsett så lenge det gjøres bytter
  SET byttet TO false  // Nullstill byttet-variabelen ved starten av hver iterasjon
  FOR hver i LESSER THAN n - 1
    IF a[i] GREATER THAN a[i+1]
      CALL byttPlass()  // Kall funksjonen for å bytte plass
      SET byttet TO true  // Sett byttet til true hvis det ble gjort bytter
    ENDIF
  ENDFOR
ENDWHILE
```


> c. Implementer pseudokoden fra punkt b i ditt programmeringsspråk. Listen skal leses inn automatisk, og den ferdig sorterte listen skal skrives til konsollet eller vises i programmet.

```psuedo
FUNCTION byttPlass()
  TEMP = a[i]
  a[i] = a[i+1]
  a[i+1] = TEMP
END FUNCTION

n = LENGTH(a)

SET i TO 0
SET byttet TO true
WHILE byttet IS true
  SET byttet TO false
  FOR hver i LESSER THAN n - 1
    IF a[i] GREATER THAN a[i+1]
      CALL byttPlass()
      SET byttet TO true
    ENDIF
  ENDFOR
ENDWHILE

FOR hver element i a
  DISPLAY element
ENDFOR
```