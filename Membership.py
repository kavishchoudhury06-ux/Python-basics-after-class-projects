m = str(input("Do you have membership (y/n): "))
m = m.lower()
if m == "y":
    sc = str(input("Are you senior citizen (y/n): " ))
    sc = sc.lower()
    if sc == "y":
        print("You get 50% membership discount + 20% Senior citizen discount")
    elif sc == "n":
        print("You get 50% membership discount only")
    else:
        print("You didnt select a valid input")
elif m == "n":
    print("You do not get any discount")
else:
    print("You didnt select a valid input")
    

        
    
