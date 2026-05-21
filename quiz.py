gameover = "no"
import random
num1 = 0
num2 = 0
increment = 0 
operation = 0
while gameover == "no":
    for i in range(1, 16):
        print(f"Question no. {i}")
        increment = random.randint(2, 30)
        num1 = num1 + increment
        increment = random.randint(2, 30)
        num2 = num2 + increment
        operation = random.randint(0, 3)
        #print(f"Operation is {operation}")
        if operation == 0:
            operation = "+"
            answer = int(input(f"{num1} {operation} {num2} is equal to: "))
            if answer == num1 + num2:
                print("You got it right!!")
            else:
                print("You got it wrong!!")
                print("Game over!")
                gameover = "yes"
                break
            if i == 10:
                gameover = "yes"
                print("You won!!")
                break
            
        elif operation == 1:
            operation = "-"
            if num2 > num1:
                temp = num2
                num2 = num1
                num1 = temp
                temp = 0 
            answer = int(input(f"{num1} {operation} {num2} is equal to: "))
            if answer == num1 - num2:
                print("You got it right!!")
            else:
                print("You got it wrong!!")
                print("Game over!")
                gameover = "yes"
                break
            if i == 10:
                gameover = "yes"
                print("You won!!")
                break
            
        elif operation == 2:
            operation = "*"
            answer = int(input(f"{num1} {operation} {num2} is equal to: "))
            if answer == num1 * num2:
                print("You got it right!!")
            else:
                print("You got it wrong!!")
                print("Game over!")
                gameover = "yes"
                break
            if i == 10:
                gameover = "yes"
                print("You won!!")
                break
            
        elif operation == 3:
            operation = "/"
            if num2 > num1:
                temp = num2
                num2 = num1
                num1 = temp
                temp = 0
            answer = int(input(f"{num1} {operation} {num2} is equal to (Without remainder): "))
            if answer == num1 // num2:
                print("You got it right!!")
            else:
                print("You got it wrong!!")
                print("Game over!")
                gameover = "yes"
                break
            if i == 10:
                gameover = "yes"
                print("You won!!")
                break
        else:
            print("Code failed")
            
    
            
                    
            

            
            
    
        