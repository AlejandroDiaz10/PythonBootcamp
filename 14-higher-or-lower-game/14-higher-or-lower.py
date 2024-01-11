# https://replit.com/@appbrewery/higher-lower-start

"""
The objective is to write a program that will compare the follower count of two Instagram accounts.
The program should ask the user to guess which account has more followers.
"""

import random
import os
from game_data import data
from art import logo, vs_logo

# Function to clear the screen
def clear_screen():
    # Detect the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Mac
        os.system('clear')

# Function to retrieve a random account from the game data
def get_random_account():
    """Get data from random account"""
    account = random.choice(data)
    # data.remove(account)
    return account

# Funtion to compare the number of followers between two accounts
def compare_accounts(account_a, account_b):
    """Compare the number of followers between two accounts"""
    if account_a["follower_count"] > account_b["follower_count"]:
        return "A"
    else:
        return "B"

# Function to play the game
def higher_or_lower_game():
    """Higher or Lower Game"""
    score = 0
    game_over = False
    account_a = get_random_account()
    account_b = get_random_account()

    print(logo)

    while not game_over:
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(vs_logo)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        clear_screen()
        print(logo)
        if guess == compare_accounts(account_a, account_b):
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b
            account_b = get_random_account()
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            print(f"-->Account A: {account_a['name']}, {account_a['follower_count']} million followers.")
            print(f"-->Account B: {account_b['name']}, {account_b['follower_count']} million followers.\n")
            game_over = True

higher_or_lower_game()