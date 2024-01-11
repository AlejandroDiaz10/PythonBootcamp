# https://replit.com/@appbrewery/oop-coffee-machine-start

"""
The goal of this project is to replicate the functionality of the coffee machine 
project (Day 15) using POO.
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("\n******************** COFFEE MACHINE ********************")

while True:
    user_input = input(f"\nWhat would you like? ({menu.get_items()}): ").lower()

    if user_input == "off":
        coffee_maker.turn_off()
        break

    elif user_input == "report":
        print("\n******************** REPORT ********************")
        coffee_maker.report()
        money_machine.report()
    
    elif user_input in menu.get_items().split("/"):
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    
    else:
        print("Sorry, that's not a valid option. Try again.")