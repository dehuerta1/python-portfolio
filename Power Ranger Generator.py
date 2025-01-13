#David Huerta
#10/18/24
#Name Generator

#Init


#Functions
def generator():
    ans = (input("Do you see yourself more as a leader or follower?"))
    if ans == "leader":
        ans = (input("Do you consider yourself to be more serious or silly?"))
        if ans == "serious":
            ans = (input("Would you be a captain or lieutenant?"))
            if ans == "captain":
                print("You Are The Red Power Ranger!")
            elif ans == "lieutenant":
                print("You Are The Blue Power Ranger!")
        elif ans == "silly":
            ans = (input("Are you rebellious or a guardian?"))
            if ans == "rebellious":
                print("You are the Silver Power Ranger!")
            elif ans == "guardian":
                print("You are the Gold Power Ranger!")
    else:
        ans = (input("Are you a loud or quiet person?"))
        if ans == "loud":
            ans = (input("Are you decisions usually cautious or impulsive?"))
            if ans == "cautious":
                print("You are the Pink Power Ranger!")
            elif ans == "impulsive":
                print("You are the Green Power Ranger!")
        elif ans == "quiet":
            ans = (input("Are you more resilient or sensitive?"))
            if ans == "resilient":
                print("You are the Black Power Ranger!")
            elif ans == "sensitive":
                print("You are the Yellow Power Ranger!")

#Main
generator()
