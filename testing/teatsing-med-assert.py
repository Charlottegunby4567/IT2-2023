# Test-drevet utvikling med assert

# En funksjon som tester om tall er partall
def partall (tall: int):
    if tall % 2 == 0:
        return True
    else:
        return False
    

assert partall(2) == True, "2 er et partall"
assert partall(1) == False, "1 er IKKE et partall"
assert partall(-2) == True, "-2 er et partall"
assert partall(-1) == False, "-1 er IKKE et partall"

