# source env/bin/activate
# pip install python-dotenv

"""
Create a letter using starting_letter.txt for each name in invited_names.txt
Replace the [name] placeholder with the actual name. Save the letters in the folder "ReadyToSend".
"""

from dotenv import load_dotenv
import os

load_dotenv()
names_absolute_path = os.getenv("NAMES_ABSOLUTE_PATH")

# Using the absolute path
# with open(names_absolute_path) as file:
#     print(file.read())

# Get the names from the file
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    # print(names)

# Get the letter
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        stripped_name = name.strip()
        letter = letter.replace("[name]", stripped_name)
        with open(
            f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w"
        ) as new_file:
            new_file.write(letter)
