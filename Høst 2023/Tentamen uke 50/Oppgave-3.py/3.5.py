def royalties(artistliste):
    tjener_per_stream = {
        "Norge": 0.55,
        "Sverige": 0.44,
        "Finland": 0.44,
        "Danmark": 0.52,
        "Island": 0.62,
        "Resten av verden (snitt)": 0.24
    }

    sum = []
    for artist, land, antall_streams in artistliste:            # artist, land og antall streams skal være i artsistlisten
        inntekt_per_sang = antall_streams * tjener_per_stream       # inntekten per sang er antall streams * det som tjenes per stream
        sum.append(inntekt_per_sang)             
    
    return sum

artister = [
    ["Sígur Ros", "Island", 1_047_010],
    ["Emma Steinbakken", "Norge",  3_459_239]
]


print(royalties(artister))  
