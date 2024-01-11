# https://replit.com/@appbrewery/coffee-machine-start

"""
The objective of this code is to write a program that will simulate a coffee machine.
1) Prompt user by asking “​What would you like? (espresso/latte/cappuccino):”​
2) Turn off the Coffee Machine by entering “​off”​ to the prompt.
3) Print report.
4) Check resources sufficient?
5) Process coins.
6) Check transaction successful?
7) Make Coffee.
8) Machine can refill resources by entering add to the prompt.
"""

from menu import MENU, resources, profit

coffee_emoji ="☕"

# Function to turn off the coffee machine
def turn_off():
    """Turns off the coffee machine"""
    print("Turning off the coffee machine...")

# Function to print the report
def print_report():
    """Prints the current resources report"""
    print("\n****************** REPORT ******************")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

# Function to check if there are enough resources to make the coffee
def check_resources(coffee):
    """Checks if there are enough resources to make the coffee"""
    for ingredient in coffee["ingredients"]:
        if coffee["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

# Function to process the coins
def process_coins(coffee, user_input):
    """Processes the coins inserted by the user"""
    global profit  # Declare profit as a global variable
    print(f"Please insert coins. The cost of the coffee selected ({user_input}) is ${coffee['cost']}")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total < coffee["cost"]:
        print(f"Sorry, that's not enough money. Money refunded: ${total}.")
        return False
    else:
        change = round(total - coffee["cost"], 2)
        print(f"Here is ${change} in change.")
        profit += coffee["cost"]
        return True

# Function to make the coffee
def make_coffee(coffee, user_input):
    """Makes the coffee"""
    for ingredient in coffee["ingredients"]:
        resources[ingredient] -= coffee["ingredients"][ingredient]
    print(f"Here is your {user_input} {coffee_emoji}. Enjoy!")

# Function to add resources to the coffee machine
def add_resources():
    """Adds resources to the coffee machine"""
    print("\n****************** ADD RESOURCES ******************")
    water = int(input("How much water would you like to add?: "))
    milk = int(input("How much milk would you like to add?: "))
    coffee = int(input("How much coffee would you like to add?: "))
    resources["water"] += water
    resources["milk"] += milk
    resources["coffee"] += coffee
    print_report()

# Function to simulate the coffee machine
def coffee_machine():
    """Simulates the coffee machine"""
    print("Welcome to the coffee machine!")
    
    while True:
        user_input = input(f"\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == "off":
            turn_off()
            break
    
        elif user_input == "report":
            print_report()
            continue

        elif user_input == "add":
            add_resources()
            continue

        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            if check_resources(MENU[user_input]):
                if process_coins(MENU[user_input], user_input):
                    make_coffee(MENU[user_input], user_input)
                    continue
                else:
                    continue
            else:
                continue
        
        else:
            print("Invalid input. Please try again.")
            continue

coffee_machine()