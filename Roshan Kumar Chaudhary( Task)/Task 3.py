print("Stop! Who would cross the Bridge of Death \nMust answer me these questions three, 'ere the other side he see.")

name = input("What is your name?")

if "arthur" in name.lower(): 
    print("My liege! You may pass!")

else:
    quest = input("What is your quest?")
    
    if "grail" not in quest.lower(): 
        print("Only those who seek the Grail may pass.")  

    else:

        colour=input("What is your favourite colour?\n")
        
        if name[0].lower()==colour[0].lower():
            print("you may pass")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
