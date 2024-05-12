while True:                                            # Dine kommentarer her
    try:                                               # 
        alder = int(input("Hvor gammel er du? "))      #
        break                                          #
    except:                                            #
        print("Ugyldig input. Alder må være et tall.") #
år = 2024                                              #
fødselsår = år - alder                                 #
print(f"Du er født i {fødselsår}")                     #