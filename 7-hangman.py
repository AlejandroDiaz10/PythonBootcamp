# Create a hangman game

# python3 -m venv env
# source env/bin/activate
# pip install Faker
# pip install Random-Word

import os
from faker import Faker
from random_word import RandomWords

def clear_screen():
    # Detect the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Mac
        os.system('clear')

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

fake = Faker()
random_word = fake.word()
r = RandomWords()
random_word = r.get_random_word()
user_guess = "_" * len(random_word)
user_lives = 6
letters_guessed = []

print(logo)
print("Mom's the word... The solution is:", random_word)

while user_lives > 0:
    letter = input("Guess your letter: ").lower()
    clear_screen()
    
    if letter in letters_guessed:
        print(f"You have already guessed the letter \"{letter}\"")
        print(user_guess)
        print(stages[user_lives])
        continue

    letters_guessed.append(letter)

    if letter in random_word:
        for i in range(len(random_word)):
            if random_word[i] == letter:
                user_guess = user_guess[:i] + letter + user_guess[i+1:]

        print(user_guess)
        print(stages[user_lives])
        if user_guess == random_word:
            print("You won!")
            break
        
    else:
        user_lives -= 1
        if user_lives == 0:
            print(stages[user_lives])
            print("You lost!")
            print(f"The word was: {random_word}")
            break
        print(f"The letter \"{letter}\" is not in the word. You lose a life.")
        print(user_guess)
        print(stages[user_lives])
