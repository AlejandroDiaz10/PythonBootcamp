# https://replit.com/@appbrewery/guess-the-number-start

"""
Create a Number Guessing Game
"""

import random
import os

logo = """
 _____ _     _____ ____  ____    _____  _     _____   _      _     _      ____  _____ ____   
/  __// \ /\/  __// ___\/ ___\  /__ __\/ \ /|/  __/  / \  /|/ \ /\/ \__/|/  _ \/  __//  __\  
| |  _| | |||  \  |    \|    \    / \  | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|  
| |_//| \_/||  /_ \___ |\___ |    | |  | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /  
\____\\____/\____\\____/\____/    \_/  \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\  
                                                                                            
"""

# Clear the screen
def clear_screen():
    # Detect the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Mac
        os.system('clear')

# Game logic
def guess_the_number_logic():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        input_number = int(input("\nMake a guess: "))

        if input_number == number:
            print("\n=========================================================")
            print("You got it, you win!")
            print(f"The answer was {number}.")
            break
        elif input_number > number:
            print("Too high.")
        elif input_number < number:
            print("Too low.")
        
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
        print("Guess again.")

    if attempts == 0:
        print("\n=========================================================")
        print("You've run out of guesses, you lose!")
        print(f"The answer was {number}.")

# Create a function to play the game
def play_guess_the_number():
    """Play the Number Guessing Game"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    while input("\nDo you want to play a game of Number Guessing? Type 'y' or 'n': ") == "y":
        clear_screen()
        guess_the_number_logic()

play_guess_the_number()