# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


def nato_alphabet():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabet are allowed!")
        nato_alphabet()
    else:
        print(output_list)


try:
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
except FileNotFoundError:
    print("File not found!")
else:
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    nato_alphabet()
