#11/20/24
#Pokemon Evolution

#Initialize
import random
#Global Variable
pokemonLevel = 0
pokemonName1 = "Pichu"
pokemonName2 = "Pickachu"
pokemonName3 = "Raichu"


#Functions

def game():
    global pokemonLevel
    global pokemonName1
    global pokemonName2
    global pokemonName3

    print("Welcome Trainer to Pokemon Evolution")
    while True:
        print("Select an activity for the day: ")
        print("""1. Train
2. Gym Battle
3. Display Pokemon Info
4. Exit""")

        option = int(input("1-4: "))
        if option == 1:
            pokemonLevel = pokemonLevel + 1
            print("Pokemon Level Increase: 1")
            print("Your Pokemon is now level " + str(pokemonLevel))

        if option == 2:
            Fight = random.randint(1,2) #integer
            if Fight == 1:
                pokemonLevel = pokemonLevel + 2
                print("You win! Pokemon Level: " + str(pokemonLevel))
            elif Fight == 2:
                pokemonLevel = pokemonLevel + 0
                print("You lost! Pokemone Level: " + str(pokemonLevel))

        if option == 3:
            if pokemonLevel < 10:
                print("Your " + pokemonName1 + " is level: " + str(pokemonLevel))

            if pokemonLevel >= 10 and pokemonLevel < 20:
                print("Your " + pokemonName2 + " is level: " + str(pokemonLevel))

            if pokemonLevel >= 20:
                print("Your " + pokemonName3 + " is level: " + str(pokemonLevel))

        if option == 4:
            print("Thank you for playing! Well see you again soon!")
#Main
game()


