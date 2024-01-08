# https://replit.com/@appbrewery/blind-auction-start

"""
The objective is to write a program that will collect the names and bids of different people. 
The program should ask for each bidder's name and their bid individually.
If there are other bidders, the screen should clear, so you can pass your phone to the next person. 
If there are no more bidders, then the program should display the name of the winner and their winning bid.
Use your knowledge of Python dictionaries and loops to solve this challenge.
"""

import os

def clear_screen():
    # Detect the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Mac
        os.system('clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

max_val = 0
bidders = {}
more_bidders = True
print("Welcome to the secret auction program.")
print(logo)
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    while True:
        if other_bidders == "yes":
            clear_screen()
            break
        elif other_bidders == "no":
            for key in bidders:
                if bidders[key] > max_val:
                    max_val = bidders[key]
                    max_value = max_val
                    max_key = key
            print(f"The winner is {max_key} with a bid of ${max_value}")
            more_bidders = False
            break
        else:
            print("Invalid input. Try again.")
            other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
            continue