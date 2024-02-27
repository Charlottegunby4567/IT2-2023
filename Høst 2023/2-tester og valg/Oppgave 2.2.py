def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d: str):
    d = d.replace("$", "") # Fjerner dollategn
    return float(d) # gjør stringen til en float og returnerer

def percent_to_float(p):
    p = p.replace("%", "") # Fjerner prosent
    return float(p) / 100 # Gjør stringen til en float, deler på 100 for å gjør tallet om til deismaltall og returnerer

main()
    
