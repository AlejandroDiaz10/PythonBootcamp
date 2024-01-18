import pandas as pd

# ===================================================================
student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for key, value in student_dict.items():
    # Access key and value
    pass

# Loop through rows of a data frame
student_data_frame = pd.DataFrame(student_dict)
for index, row in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# ===================================================================
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# nato_dictionary = nato_data.to_dict() - doesn't work
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = [
    nato_dictionary[letter.upper()] if letter.upper() in nato_dictionary else letter
    for letter in input("Give a word/name to NATO code: ")
]
print(user_input)
