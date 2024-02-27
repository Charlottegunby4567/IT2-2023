# få ut de som ikke har over 100 000 000 streams. 
def populære(artistliste):
    populære_artister = [artist for artist in artistliste if artist[1] > 100_000_000]
    return populære_artister

artister = [
    ["Taylor Swift",  109_940_000],
    ["The Weeknd",    105_410_000],
    ["Justin Bieber",  83_820_000],
    ["Drake",          81_980_000],
    ["Ariana Grande",  81_800_000]
]

print(populære(artister))  



