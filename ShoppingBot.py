#importing required libraries
import re
from colorama import Fore, Style, init
import time
import numpy as np
from textblob import TextBlob
import random

#autoreset
init(autoreset=True)

def get_percent(x,y):
    return (x/100)*y

def sleep(word):
    
    
    print(word,end="")
        
    for _ in range(3):
        print("",end=".")
        secs = random.uniform(0.2,0.4)

        time.sleep(secs)
    print()
         
    
    

#normalizing input using regular expression
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

#function for easy use of colorama
def printf(color, text):
    if color.lower() == "cyan":
        print(f"{Fore.CYAN} {text}")
    elif color.lower() == "red":
        print(f"{Fore.RED} {text}")
        
    elif color.lower() == "lime":
        print(f"{Fore.GREEN} {text}")
        
    elif color.lower() == "yellow":
        print(f"{Fore.YELLOW} {text}")

#Empty bill, pre-defined coupons to be used by user 
   
bill = []
coupons = {"ORDER20" : 20,
           "FIRSTORDER" : 30,
           "NEWCUSTOMER" : 35,
           "ORDER10" : 10,
           "FRIENDREFERRAL" : 25,
           "HAPPYHOURS" : 15}

#function to place order for specific item and quantity, adds it to the bill

def place_order(item, number):
    stock = items.get(item)

    if stock-number < 0 or number<0:
        return "Invalid"
    else:
        newstock = stock-number
        items[item] = newstock
        price = prices.get(item)
        bill.append(item)
        bill.append(number)
        bill.append(price)
        return "valid"
    
#function to print the bill in a tabular format 
def showbill(discount,tip):
    
    prices = []
    if not bill == []:
        print(f"{Fore.LIGHTCYAN_EX}{"item":<15} {"qty":<15} {"price":<15}")
        for i in range(0, len(bill), 3):
            item, qty, price = bill[i:i+3]
            prices.append(price*qty)
            totals = np.array(prices)
            
            
            
            print(f"{Fore.LIGHTMAGENTA_EX}{item:<15} {qty:<15} {price*qty:<15}")
        subtotal = totals.sum()
        CGST = 5
        SGST = 5
        Tip = 15
        
        discounted_price = subtotal-get_percent(subtotal,discount)
        tax = get_percent(discounted_price,CGST)+get_percent(discounted_price,SGST)
        current_discount = get_percent(subtotal,discount)
        servicetip = get_percent(discounted_price,Tip)
        
        
        print(f"{Fore.GREEN}{"Subtotal":<15} {"":<15} {totals.sum():<15}")
        print(f"{Fore.GREEN}{"Discount":<15} {"":<15} {current_discount:.2f} ({discount}%)")
        if tip == True:
            grand_total = discounted_price+tax+servicetip
            print(f"{Fore.GREEN}{"Tip":<15} {"":<15} {Tip}%")
        else:
            grand_total = discounted_price+tax
        print(f"{Fore.GREEN}{"CGST":<15} {"":<15} {CGST}%")
        print(f"{Fore.GREEN}{"SGST":<15} {"":<15} {SGST}%")
        print(f"{Fore.GREEN}{"Total":<15} {"":<15} {grand_total:<10.2f}")
    else:
        printf("red", "The bill is empty")

#function to show all items and prices and quanities        
def show_cart():
    if not bill == []:
        print(f"{Fore.LIGHTCYAN_EX}{"item":<15} {"qty":<15} {"price":<15}")
        for i in range(0, len(bill), 3):
            item, qty, price = bill[i:i+3]
            print(f"{Fore.LIGHTMAGENTA_EX}{item:<15} {qty:<15} {price*qty:<15}")
    else:
        printf("red","You have not ordered anything")

#function to show the current cart total
def show_total():
    if bill:
        prices = []
        for i in range(0, len(bill), 3):
            item, qty, price = bill[i:i+3]
            prices.append(price*qty)
            totals = np.array(prices)
        return totals.sum()
    else:
        return 0
    
        
#function for the user name and help instructions at start       
def intro():
    
    global name
    print(f"{Fore.CYAN} Welcome To Our Shop!{Style.RESET_ALL}")
    name = input(f"{Fore.CYAN}Enter your Name: {Style.RESET_ALL}").capitalize()
    print(f"{Fore.CYAN}Nice To Meet You {name}!{Style.RESET_ALL}")
    text = "-Type 'Exit' to close \n-Type 'Stock' to see the stock\n-Type 'Refresh' to renew items\n-Type 'Order' to place an order\n-Type 'Dishes' to view your added items\n-Type 'Random' to generate a random simulation\n-Type 'Total' to see your cart total\n-Type 'Cancel' to cancel all orders"
    printf("yellow",text)
    
#function to apply coupon code to bill   
def apply_discount():
    global dis
    disc = input(f"{Fore.MAGENTA}Do you have any coupon code? (y/n): ")
    disc = normalize_input(disc)
    if "y" in disc:
        disc = input(f"{Fore.BLUE}Please enter a coupon: ")
        sleep("Processing")
        disc= normalize_input(disc)
        disc = disc.upper()
        if disc in coupons:
            dis = coupons.get(disc)
        else:
            printf("red", "Sorry, this is an invalid coupon code")
            apply_discount()
    else:
        dis = 0
        
#function to clear the cart       
def clear_cart():
    global bill
    bill = []


#dict for items and prices,menu courses   
global items
items = {
    "pizza": 20,
    "burger": 25,
    "pasta": 15,
    "salad": 30,
    "coffee": 50,
    "tea": 60,
    "icecream": 40,
    "cake": 10,
    "soup": 20,
    "sandwich": 25,
    "biryani": 18,
    "fried_rice": 22,
    "noodles": 20,
    "paneer_tikka": 15,
    "chicken_curry": 12,
    "fish_fry": 10,
    "lassi": 35,
    "juice": 40,
    "brownie": 20,
    "milkshake": 25
}


prices = {
    "pizza": 250,
    "burger": 180,
    "pasta": 220,
    "salad": 150,
    "coffee": 80,
    "tea": 60,
    "icecream": 120,
    "cake": 200,
    "soup": 130,
    "sandwich": 160,
    "biryani": 300,
    "fried_rice": 200,
    "noodles": 190,
    "paneer_tikka": 240,
    "chicken_curry": 280,
    "fish_fry": 260,
    "lassi": 90,
    "juice": 100,
    "brownie": 150,
    "milkshake": 140
}

courses = {
    "starter": ["soup", "salad", "sandwich", "paneer_tikka", "fish_fry"],
    "maincourse": ["pizza", "burger", "pasta", "biryani", "fried_rice", "noodles", "chicken_curry"],
    "dessert": ["icecream", "cake", "brownie"],
    "drink": ["coffee", "tea", "lassi", "juice", "milkshake"]
}



#function to print all items and quantities in a line-by-line manner
def stock(course):
    dishes = courses.get(course)
    if dishes:
        print()
        printf("cyan",f"{course}:- ")
        for i in dishes:
            printf("lime",f"{i} : {items.get(i)}")

item_reset = items.copy()
item_keys = list(items.keys())

#functions for randomizing order
def get_num():
    global order,num
    order = random.choice(item_keys)
    try:
        num = random.randint(1, items.get(order))
    except:
        get_num()  
def ran():
    get_num()
    place_order(order, num)
    printf("lime", f"Placed {num} {order}(s)")
def random_order(number):
    for _ in range(number):
        ran()
        
def recommend(course):
    return random.choice(courses.get(course))

#function to check if user has entered any valid dish       
def orderitem(userinput):
                        
    global current_item
    current_item = ""                  
    itemsr = items.copy()
              
    s = userinput.split()
    k = itemsr.keys()
    for i in s:
        if i in k:
            current_item = i
            break
        else:
            current_item = ""
                                    


    if current_item == "":
        return "Invalid"
        
                                
    else:
        return current_item
        
#function to check for valid number       
def ordernumber(number):
    if number.isdigit():
        return int(number)
    else:
        return "Invalid"
    
#Structural function for placing order   
def helper(c):
            stock(str(c))
            printf("lime",f"Please order a {c} ")
            printf("cyan",f"We recommend: {recommend(c)}")
            user = input(f"{Fore.WHITE}{name}: ")
            sleep("Processing")
            userinput = normalize_input(user)
            val = orderitem(userinput)
            if val == "Invalid":
                printf("red","You cannot order this item")
            else:
                useritem = val
                printf("lime","How many?")
                
                user = input(f"{Fore.WHITE}{name}: ")
                sleep("Processing")
                userinput = normalize_input(user)
                val = ordernumber(userinput)
                if val == "Invalid":
                    printf("red","Invalid input")
                else:
                    usernumber = userinput
                    val = place_order(useritem,int(usernumber))
                    if val == "Invalid":
                        printf("red","Invalid input")
                    else:
                        printf("lime",f"Placed an order for {usernumber} {useritem}(s)")

#function to call as per different courses                            
def take_order():
    while True:
        printf("cyan","What would you like to order? (Starters, Mains, Drinks, Deserts)")
        user = input(f"{Fore.WHITE}{name}: ")
        sleep("Processing")
        userinput = normalize_input(user)
        if "starter" in userinput:
            helper("starter")        
        elif "maincourse" in userinput:
            helper("maincourse")
        elif "drink" in userinput:
            helper("drink")
        elif "dessert" in userinput:
            helper("dessert")
        else:
            printf("red","Invalid input")
            break
        
        


#main loop
def main():
    while True:
        user = input(f"{Fore.WHITE}{name}: ")
        sleep("Processing")
        userinput = normalize_input(user)
        
        if "dishes" in userinput:
            show_cart()
        elif "total" in userinput:
            printf("cyan", show_total())
            
        elif "refresh" in userinput:
            global items
            items = item_reset
            for course in courses:
                stock(course)
        elif "stock" in userinput:
            for course in courses:
                stock(course)
        elif "cancel" in userinput:
            clear_cart()
        elif "order" in userinput:  
            take_order()
        elif "exit" in userinput:
            #using textblob, retrieve a feedback and analyse, apply coupons and dicount codes using apply_discount() method
            printf("lime", "Please leave us a feedback before closing!")
            inp = input(f"{name}: ")
            polarity = TextBlob(inp).sentiment.polarity
            if polarity > 0.25:
                printf("lime","Thank you for the wonderful feedback!")
            elif polarity < -0.25:
               printf("red","We are so sorry for your experince with us")
            else:
                printf("Yellow","Thanks, hope you had a great experince with us")
            apply_discount()
            tip = input(f"{Fore.MAGENTA}Would you like to leave a tip? (y/n): ")
            if "y" in tip:
                printf("cyan","Your Bill-")
                showbill(dis,True)
                break
            else:
                printf("cyan","Your Bill-")
                showbill(dis,False)
                print()
                printf("lime", "Thank you for dining with us!")
                break
               
        elif "random" in userinput:
            #to get number of random orders to be generated from the user
            numofsims = input(f"{Fore.CYAN}How many items do you want to be ordered?: ")
            try:
                random_order(int(numofsims))
            except:
                pass
        else:
            printf("red", f"I could not understand you, {name}. Could you rephrase?")  

#to run mainloop    
if __name__ == "__main__": 
    intro()
    main()   