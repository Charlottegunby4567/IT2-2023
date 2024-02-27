# Oppgave 2.1: Variabler


#1 Lag et program som skriver ut ”Zup buddy?” i terminalen.
print("Zup Buddy!")


#2 Endre programmet slik at du ber brukeren om å oppgi et 
# navn i form av en tekststreng ved hjelp av funksjonen input(), 
# og lagre denne verdien i en variabel navn. Skriv så ut “Zup “ 
# og variabelen navn
navn = input ("Hva heter du?")
print("Zup", navn + "?")


#3 Be bruker om å oppgi enda et navn, og print ut "Zup" 
# etterfulgt av begge navnene, med "og" mellom. 
# For eksempel slik “Zup ola og kari?”.
navn1 = input ("Hva heter du?")
navn2 = input("Hva med deg?")


#4 Legg til kode slik at navnene printes med stor forbokstav, 
# uansett hva brukeren har skrevet inn. For eksempel hvis 
# brukeren skriver inn "ola" og "kari", skal det printes 
# "Zup Ola og Kari?
navn1 = input("Hva heter du? ")
navn2 = input("Hva med deg? ")
navn1 = navn1.title()
navn2 = navn2.title()
print("Zup", navn1, "og", navn2 + "?")


