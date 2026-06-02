num = int(input("Enter a starting number for the countdown: "))

def countdown(num):
    
    if num <= 0:
        print("countdown over")
    else:
        print(num, end=" ")
        countdown(num-1)
        
countdown(num)
    