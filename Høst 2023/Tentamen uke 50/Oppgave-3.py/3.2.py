
Trinn_1 = 399_999
Trinn_2 = 1_400_000 + 29_999_999 * 0.40
Trinn_3 = 30_000_000 + 30_000_000 * 0.70


def andel_til_artist(antall_streams: int):
    if antall_streams <= Trinn_1:
        return "0"
    
    if antall_streams <=  Trinn_2:
        return "0.40"
    
    if antall_streams <= Trinn_3:
        return "0.70"
    


print (andel_til_artist(50_000))
print (andel_til_artist(5_000_000))
print (andel_til_artist(50_000_000))



