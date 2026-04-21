import random
Plr = random.randint(1, 6)
Com = random.randint(1, 6)

if Plr > Com:
    print("You win!")
elif Plr < Com:
    print("Computer wins!")
else:
    print("It is a tie!")