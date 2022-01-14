convert_to_km=lambda speed:speed*1.60934
MPH=[]

print("Swallow Speed Analysis: Version 1.0\n")

while True:
    input_by_user=input("Enter the speed:")
    if input_by_user=="":  
        break

    if (input_by_user[0].lower()!="u" and input_by_user[0].lower()!="e") or input_by_user[1:].isalpha():
        print("Invalid input")
        continue

    speed=float(input_by_user[1:]) 

    if input_by_user[0].lower()=="u":
        MPH.append(speed)

    else:
        speed*=0.621371
        MPH.append(speed)

    print("Reading saved.")

if MPH!=[]:
    max_val=max(MPH) 
    min_val=min(MPH) 
    avg_val=sum(MPH)/len(MPH)
    print("\nResults Summary\n")
    if len(MPH)==1:
        print("{} Reading Analysed.\n".format(len(MPH)))
    else:
        print("{} Readings Analysed.\n".format(len(MPH)))
    
    print("Max Speed:{:.2f}MPH,{:.2f}KPH".format(max_val,convert_to_km(max_val)))
    print("Min Speed:{:.2f}MPH,{:.2f}KPH".format(min_val,convert_to_km(min_val)))
    print("Avg Speed:{:.2f}MPH,{:.2f}KPH".format(avg_val,convert_to_km(avg_val)))

else:
    print("No readings entered. Nothing to do.") 
        
    
