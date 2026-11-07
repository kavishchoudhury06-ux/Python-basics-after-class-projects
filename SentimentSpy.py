from textblob import TextBlob
import colorama
from colorama import Fore, Style
g = -1
print(f"{Fore.LIGHTRED_EX} Welcome to the application{Style.RESET_ALL}")
moods = []
while True:
    userinput = str(input(f"{Fore.LIGHTCYAN_EX}Please type something: "))
    
    polarity = TextBlob(userinput).sentiment.polarity
    
    
    if polarity > 0.25:
        mood = "happy"
        moods.append(mood)
        
    elif polarity > -0.25 and polarity <0.25:
        mood = "ok"
        moods.append(mood)
        
    elif polarity < -0.25:
        mood = "sad"
        moods.append(mood)
    
    if not userinput:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    if userinput.lower() == "exit":
        print(Fore.GREEN, "Generating report...", Style.RESET_ALL)
        for i in enumerate(moods, start=0):
            g = g+1
            print(f'{Fore.GREEN}{g+1}: {moods[g]}')
        print(f" {Fore.GREEN}User is happy in {moods.count("happy")} inputs")
        print(f"{Fore.RED}User is sad in {moods.count("sad")} inputs")
        print(f"{Fore.YELLOW}User is ok in {moods.count("ok")} inputs")
        
        
        print(f"\n{Fore.BLUE}Exiting... {Style.RESET_ALL}")
        break
    
    print(f"Your mood is: {mood}")
    