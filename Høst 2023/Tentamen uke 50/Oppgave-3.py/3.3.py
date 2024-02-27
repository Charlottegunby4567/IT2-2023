
def per_stream(land):
    tjener_per_stream = {
        "Norge": 0.55,
        "Sverige": 0.44,
        "Finland": 0.44,
        "Danmark": 0.52,
        "Island": 0.62,
        "Resten av verden (snitt)": 0.24
    }

    return tjener_per_stream.get(land, 0.24)

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
    
# (antall streams * penger per stream * andel til artist)


def penger_tjent(antall_streams, land):
        antall_streams * land


print(penger_tjent(5_000_000, "Norge"))     # 1 100 000
print(penger_tjent(100_000_000, "Island"))  # 43 400 000


# SKJØNNER IKKE, JEG FÅR DET IKKE TIL, JEG FÅR BARE NONE