import random
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

choices = ["rock", "paper", "scissors"]

def ai_move(last_player_choice):
    if last_player_choice is None:
        return random.choice(choices)
    if last_player_choice == "rock":
        return "paper"
    elif last_player_choice == "paper":
        return "scissors"
    elif last_player_choice == "scissors":
        return "rock"

def winner(player, ai):
    if player == ai:
        return Fore.YELLOW + "It's a tie!" + Style.RESET_ALL
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return Fore.GREEN + "You win!" + Style.RESET_ALL
    else:
        return Fore.RED + "AI wins!" + Style.RESET_ALL

def play():
    print(Fore.CYAN + "Welcome to Rock-Paper-Scissors with AI!" + Style.RESET_ALL)
    last_player_choice = None
    
    while True:
        player = input(Fore.BLUE + "Choose rock, paper, or scissors (or quit): " + Style.RESET_ALL).lower()
        if player == "quit":
            print(Fore.MAGENTA + "Thanks for playing!" + Style.RESET_ALL)
            break
        if player not in choices:
            print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)
            continue
        
        ai = ai_move(last_player_choice)
        print(Fore.CYAN + f"AI chose: {ai}" + Style.RESET_ALL)
        print(winner(player, ai))
        
        last_player_choice = player

play()
