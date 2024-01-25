import sys
from tkinter import *
import pandas as pd
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
FONT_STYLE = ("Helvetica", 25)

data = []
unknown_words = []
words_used = []
selected_word = {}

# ================================================= Reset global variables
def reset_global_variables():
    global data, unknown_words, words_used, selected_word
    data = []
    unknown_words = []
    words_used = []
    selected_word = {}

# ================================================= Show appropriate buttons 
def show_buttons(state):
    if state == "off":
        right_button.grid_forget()
        wrong_button.grid_forget()

        new_game_button.grid(row=1, column=0, columnspan=2)
        try:
            data_read = pd.read_csv("./data/unknown_words.csv")
        except (FileNotFoundError, pd.errors.EmptyDataError):
            pass
        else:
            resume_game_button.grid(row=2, column=0, columnspan=2)
        finally:
            window.update_idletasks()
    else:
        new_game_button.grid_forget()
        resume_game_button.grid_forget()

        right_button.grid(row=1, column=1)
        wrong_button.grid(row=1, column=0)
        select_new_word()

# ================================================= Read file (new game)
def new_game():
    reset_global_variables()
    global data
    try:
        data = pd.read_csv("./data/french_words.csv").to_dict(orient="records")
    except FileNotFoundError:
        print("File wasn't found")
        sys.exit(1)
    else:
        show_buttons("on")

# ================================================= Read file (unknown words from previous game)
def resume_game():
    reset_global_variables()
    global data
    try:
        data = pd.read_csv("./data/unknown_words.csv").to_dict(orient="records")
    except FileNotFoundError:
        print("File wasn't found")
    else:
        show_buttons("on")

# ================================================= Create CSV file ofunknown words
def write_to_csv():
    df = pd.DataFrame(unknown_words)
    df.to_csv("./data/unknown_words.csv", index=False, encoding="utf-8")
    
# ================================================= Keep track of users choice
def user_choice(choice):
    if choice == "right":
        pass
    elif choice == "wrong":
        unknown_words.append(selected_word)
    select_new_word()

# ================================================= Select new word
def select_new_word():
    canvas.itemconfig(language_cv, text="French", fill="black")
    canvas.itemconfig(img_cv, image=front_img)
    if len(words_used) == len(data):
        canvas.itemconfig(count_cv, text="No more words in the list", fill="black")
        write_to_csv()
        show_buttons("off")
    else:
        # Select a random word
        index = randint(0, len(data) - 1)
        while index in words_used:
            index = randint(0, len(data) - 1)
        
        # Set the timer
        words_used.append(index)
        global selected_word
        selected_word = data[index]
        canvas.itemconfig(word_cv, text=f"{selected_word.get("French")}", fill="black")
        canvas.itemconfig(count_cv, text=f"Remaining words: {len(data) - len(words_used)}", fill="black")
        right_button.config(state="disabled")
        wrong_button.config(state="disabled")
        window.after(2000, turn_back_card)

# ================================================= Show answer
def turn_back_card():
    canvas.itemconfig(word_cv, text=f"{selected_word.get("English")}", fill="white")
    canvas.itemconfig(language_cv, text="English", fill="white")
    canvas.itemconfig(count_cv, fill="white")
    canvas.itemconfig(img_cv, image=back_img)
    right_button.config(state="active")
    wrong_button.config(state="active")

# ================================================= UI
# Window
window = Tk()
window.title("Learn French With Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=900, height=626)

# Canvas
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_cv = canvas.create_image(400, 263, image=front_img)

# Canvas text
language_cv = canvas.create_text(
    400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic")
)
word_cv = canvas.create_text(
    400, 263, text="word", fill="black", font=(FONT_NAME, 60, "bold")
)
count_cv = canvas.create_text(
    400,
    470,
    text=f"Remaining words: {len(data) - len(words_used)}",
    fill="black",
    font=(FONT_NAME, 20),
)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(
    image=wrong_img,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    bg=BACKGROUND_COLOR,
    command=lambda: user_choice("wrong"),
)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(
    image=right_img,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    bg=BACKGROUND_COLOR,
    command=lambda: user_choice("right")
)

new_game_button = Button(
    text="New Game",
    highlightbackground=BACKGROUND_COLOR,
    bg=BACKGROUND_COLOR,
    width=30,
    font=FONT_STYLE,
    command=new_game
)

resume_game_button = Button(
    text="Try previous words",
    highlightbackground=BACKGROUND_COLOR,
    bg=BACKGROUND_COLOR,
    width=30,
    font=FONT_STYLE,
    command=resume_game
)

show_buttons("off")

window.mainloop()
