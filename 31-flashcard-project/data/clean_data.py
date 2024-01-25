# File: https://github.com/hermitdave/FrequencyWords/blob/master/content/2018/fr/fr_50k.txt

# source env/bin/activate
# pip install --upgrade googletrans==4.0.0-rc1

import sys
from googletrans import Translator
import pandas as pd


def read_file():
    try:
        with open("fr_50k.txt") as file:
            words_list = file.readlines()
    except FileNotFoundError as e:
        print("File not founded")
        print(f"An exception occurred: {str(e)}")
        sys.exit(1)
    else:
        return words_list


def clean_data():
    raw_words = read_file()
    french_words = [word.split()[0] for word in raw_words]
    return french_words


def translate_words(french_words):
    translator = Translator()
    translated_words = [
        translator.translate(word, src="fr", dest="en").text for word in french_words
    ]
    return translated_words


def create_csv_file(french_words, english_translations):
    df = pd.DataFrame(
        list(zip(french_words, english_translations)), columns=["French", "English"]
    )
    df.to_csv("translations.csv", index=False, encoding="utf-8")


french_words = clean_data()[:50]
english_words = translate_words(french_words)
create_csv_file(french_words, english_words)
