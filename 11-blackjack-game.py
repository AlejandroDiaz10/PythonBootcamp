# https://replit.com/@appbrewery/blackjack-start

"""
Develop a Blackjack game
"""

import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Clear the screen
def clear_screen():
    # Detect the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Mac
        os.system('clear')

# Create and shuffle the deck of cards (52 cards)
def create_deck():
    """Returns a shuffled deck of cards."""
    standard_suits = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    cards = standard_suits * 4
    random.shuffle(cards)
    return cards

# Deal the cards to the user and the computer
def deal_card(cards):
    """Returns a random card from the deck.""" 
    # Despite the fact that the cards are shuffled, we can still use the random.choice() 
    # function to pick a random card from the deck.
    card = random.choice(cards)
    # Remove the card from the deck
    cards.remove(card)
    return card

# Calculate the score of the user and the computer
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Verify if there is a face card (J, Q, K) and replace with a float value
    # in order to keep track of the original card
    # Verify if there is an Ace (A) and replace with a 11 value
    for card in cards:
        if card == "J":
            cards[cards.index(card)] = 10.1
        elif card == "Q":
            cards[cards.index(card)] = 10.2
        elif card == "K":
            cards[cards.index(card)] = 10.3
        elif card == "A":
            cards[cards.index(card)] = 11
    
    # Determine if we won (1), lost (0) or still playing (score)
    score = int(sum(cards))
    if score > 21:
        for card in cards:
            if card == 11:
                # Edge case: there is more than one Ace (A) in the hand
                score = int(sum(cards))
                if score > 21:
                    cards[cards.index(card)] = 1
                    score = int(sum(cards))
    return int(score)



# Show the cards of the user and the computer
def show_cards(cards):
    """Show the cards of the user and the computer"""
    for card in cards:
        if card == 10.1:
            cards[cards.index(card)] = "J"
        elif card == 10.2:
            cards[cards.index(card)] = "Q"
        elif card == 10.3:
            cards[cards.index(card)] = "K"
        elif card == 11 or card == 1:
            cards[cards.index(card)] = "A"
    return cards

# Compare the scores of the user and the computer
def compare(user_score, computer_score):
    """Compare the scores of the user and the computer"""
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 21:
        return "You lose, opponent has Blackjack!"
    elif user_score == 21:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You lose, you went over!"
    elif computer_score > 21:
        return "You win, opponent went over!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

# Blackjack game logic
def blackjack_logic(deck):
    """This is the Blackjack game logic"""
    # Deal the cards to the user and the computer
    uc_1 = deal_card(deck)
    cc_1 = deal_card(deck)
    uc_2 = deal_card(deck)
    cc_2 = deal_card(deck)
    user_cards = [uc_1, uc_2]
    computer_cards = [cc_1, cc_2]

    # Show the cards of the user and the computer
    user_score = calculate_score(user_cards)
    user_hand = show_cards(user_cards)
    print(f"Your cards: {user_hand} \t Current score: {user_score}")
    computer_score = calculate_score(computer_cards)
    computer_hand = show_cards(computer_cards)
    print(f"Computer's first card: {[computer_hand[0]]}")

    # Check if the user or the computer has a Blackjack
    if user_score == 21 and computer_score != 21:
        return user_hand, computer_hand, "You win, you have a natural Blackjack"
    elif computer_score == 21 and user_score != 21:
        return user_hand, computer_hand, "You lose, opponent has a natural Blackjack"
    elif user_score == 21 and computer_score == 21:
        return user_hand, computer_hand, "It's a draw, both have a natural Blackjack"
    
    # User plays
    while user_score != 21 and user_score < 21:
        # Ask the user if he wants to draw another card
        if input("\nType 'y' to get another card, type 'n' to pass: ") == "y":
            user_cards.append(deal_card(deck))
            user_score = calculate_score(user_cards)
            user_hand = show_cards(user_cards)
            print(f"Your cards: {user_hand} \t\tCurrent score: {user_score}")

        else:
            break
    
    # Computer plays - Dealer has to hit until it reaches at least 17
    print(f"Computer's cards: {computer_hand} \t\tCurrent score: {computer_score}")
    while computer_score != 21 and computer_score < 17:
        if computer_score >= 21:
            break

        # if computer_score > user_score or user_score > 21:
        #     break

        computer_cards.append(deal_card(deck))
        computer_score = calculate_score(computer_cards)
        computer_hand = show_cards(computer_cards)
        print(f"Computer's cards: {computer_hand} \t\tCurrent score: {computer_score}")
    
    user_result = [user_hand, user_score]
    computer_result = [computer_hand, computer_score]

    return user_result, computer_result, compare(user_score, computer_score)

def play_blackjack():
    """Play the Blackjack game"""
    print(logo)
    print("The goal is to get as close to 21 as possible, without going over.\n")
    print("* Cards 2-10 are worth their face value.")
    print("* J, Q, and K are each worth 10.")
    print("* Aces are worth 1 or 11.\n")

    # Create the deck of cards
    deck = create_deck()

    # Play the Blackjack game
    while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y" and len(deck) > 6:
        clear_screen()
        user, computer, result = blackjack_logic(deck)
        print("\n=========================================================")
        print(f"Your final hand: {user[0]} \t\tFinal score: {user[1]}")
        print(f"Computer's final hand: {computer[0]} \t\tFinal score: {computer[1]}")
        print(f"-->{result}")

    # Reshuffle the deck if wished
    if len(deck) <= 6:
        print("\n======================= WARNING =========================")
        print("There are not enough cards to play a game of Blackjack!")
        if input("Would you like to reshuffle the deck? Type 'y' or 'n': ") == "y":
            play_blackjack()

    print("\nThanks for playing! Goodbye!")

play_blackjack()