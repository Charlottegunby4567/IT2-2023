# 3.1 - Penger per stream

def per_stream(land):
    tjener_per_stream_land = {
        "Norge": 0.55,
        "Sverige": 0.44,
        "Finland": 0.44,
        "Danmark": 0.52,
        "Island": 0.62,
        "Resten av verden (snitt)": 0.24
    }

    return tjener_per_stream_land.get(land, 0.24)

print(per_stream("Norge"))
print(per_stream("Island"))
print(per_stream("USA"))    




