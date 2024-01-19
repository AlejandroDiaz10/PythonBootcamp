from tkinter import *

# Create the window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

# Create the labels
label_is_equal = Label(text="is equal to")
label_is_equal.grid(row=1, column=0)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

label_res = Label(text="0")
label_res.grid(row=1, column=1)

# Create the entry
entry = Entry(width=5)
entry.insert(END, string="0")
entry.grid(row=0, column=1)


# Create the function
def miles_to_km():
    res = int(entry.get()) * 1.609
    label_res.config(text="{:.2f}".format(res))


# Create the button
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)


# Keep the window open
window.mainloop()
