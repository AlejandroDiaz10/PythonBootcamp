# source env/bin/activate
# pip install pyperclip
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# pyperclip.copy('The text to be copied to the clipboard.')
# pyperclip.paste()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    pwd_letters = [choice(letters) for _ in range(randint(8, 10))]
    pwd_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pwd_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pwd_letters + pwd_symbols + pwd_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pwd_entry.delete(0, END)
    pwd_entry.insert(END, string=f"{password}")
    pyperclip.copy(password)  # Test it with Command + V


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    website = website_entry.get()
    username = user_name_entry.get()
    pwd = pwd_entry.get()

    if website == "" or username == "" or pwd == "":
        messagebox.showerror(
            title="Missing Data", message="Don't leave any fields empty"
        )

    else:
        is_correct = messagebox.askokcancel(
            title=website,
            message=f"Website: {website} \nEmail: {username} \nPassword: {pwd} \n\nIs the information provided correct? ",
        )

        if is_correct:
            with open("pwd_data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {pwd}\n")

            website_entry.delete(0, END)
            user_name_entry.delete(0, END)
            pwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
padlock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

user_name_label = Label(text="Email/Username:")
user_name_label.grid(row=2, column=0, sticky="e")

pwd_label = Label(text="Password:")
pwd_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=38)
website_entry.insert(END, string="")
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")

user_name_entry = Entry(width=38)
user_name_entry.insert(END, string="")
user_name_entry.grid(row=2, column=1, columnspan=2, sticky="w")

pwd_entry = Entry(width=20)
pwd_entry.insert(END, string="")
pwd_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_pwd_button = Button(text="Generate Password", width=12, command=generate_pwd)
generate_pwd_button.grid(row=3, column=2, sticky="w")

add_pwd_button = Button(text="Add", width=35, command=save_pwd)
add_pwd_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
