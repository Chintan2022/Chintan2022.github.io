# Snake_Water_Gun Game

"""
1 for Snake
-1 for Water
0 for Gun
"""

import random
import os

game_dict = {"Snake": 1, "Water": -1, "Gun": 0}
reverse_game_dict = {1: "Snake", -1: "Water", 0: "Gun"}

def clear_screen():
    """clearing the console screen....."""
    """code found in the OS module"""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def game():
    """Main game Function..."""
    clear_screen()
    print("\n***** Hello Welcome to the Snake🐍 - Water💧 - Gun🔫 Game *****\n")
    print("The choices are:")
    for key, value in game_dict.items():
        print(f"{key} is {value}")

    try:
        user_choice = int(input("\nPlease Enter Your Choice (1 for Snake, -1 for Water, 0 for Gun): "))
    except ValueError:
        """handling ValueError"""
        print("Invalid input! Please enter a number (1, -1, 0).")
        return

    if user_choice not in [1, 0, -1]:
        print("Sorry, you have entered an invalid choice. Please try again.")
        return

    computer_choice = random.choice([1, 0, -1])
    print(f"""\nYou Chose ---> {reverse_game_dict[user_choice]}\nThe Computer Chose ---> {reverse_game_dict[computer_choice]}\n""")

    if user_choice == computer_choice:
        print("Well...Well...Well...!!! It's a Draw!!!!!")
    else:
        if user_choice == 1:  # Snake
            if computer_choice == 0:  # Snake vs Gun
                print("Gun shoots and kills the Snake.")
                print("You Lose!")
            elif computer_choice == -1:  # Snake vs Water
                print("Snake drinks the Water.")
                print("You Win!")
        elif user_choice == -1:  # Water
            if computer_choice == 1:  # Water vs Snake
                print("Snake drinks the Water.")
                print("You Lose!")
            elif computer_choice == 0:  # Water vs Gun
                print("Water destroys the Gun.")
                print("You Win!")
        elif user_choice == 0:  # Gun
            if computer_choice == 1:  # Gun vs Snake
                print("Gun shoots and kills the Snake.")
                print("You Win!")
            elif computer_choice == -1:  # Gun vs Water
                print("Water destroys the Gun.")
                print("You Lose!")
def game_continuation():
    """For continuing the Game or to Exit the Game"""
    while True:
        choice = input("\nDo you want to continue? (Y/N): ").lower()
        if choice=="y" or choice=="n":
            return choice
        else:
            print("Invalid input! Please enter 'Y' or 'N'.")

# Main Game Starts
game_on = True

while game_on:
    game()
    user_input = game_continuation()
    if user_input == "n":
        clear_screen()
        print("Thanks for playing! Goodbye!")
        game_on = False
