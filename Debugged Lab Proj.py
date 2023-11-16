# import the modules and packages needed for program execution
import tkinter as tk
from tkinter import *
import string
import random
import pyperclip

# creates a window with its title and modified the window's size and background
window = Tk()
window.title("Random Password Generator")
window.resizable(width=False, height=False)
window.config(bg="#FFF3E2")

# creates a label, modifies the background, font, and placement of the label in the window
lbl_welcome = Label(master=window, text="WELCOME TO THE PASSWORD GENERATOR!", bg="#FFF3E2", font=("Arial", 20, "bold"))
lbl_welcome.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=15, pady=15)

# creates a label, modifies the background, font, and placement of the label in the window
lbl_choose = Label(master=window, text="Choose the length of your password:", bg="#FFF3E2", font=("Arial", 10, "bold"))
lbl_choose.grid(row=2, column=0, columnspan=3, sticky='nsew', padx=20, pady=20)

# creates a slider with an initial value of 4, with the slider's values ranging from 4 to 50
# modifies its placement and color
slider_var = IntVar()
slider_var.set(4)
slider = Scale(window, from_=4, to=50, orient=tk.HORIZONTAL, variable=slider_var)
slider.grid(row=3, column=0, columnspan=3, sticky='nsew', padx=15, pady=10)
slider.config(bg="#FFF3E2", activebackground='#E74646')

# creates a label, modifies the background, font, and placement of the label in the window
lbl_choosechar = Label(master=window, text="Choose what to include in your password:", bg="#FFF3E2", font=("Arial", 10, "bold"))
lbl_choosechar.grid(row=5, column=0, columnspan=3, sticky='nsew', padx=10, pady=15)

# creates instances of the choices, StringVar() helps to control the widget's state, sets its initial value to 0 or off
varc1 = StringVar()
varc1.set("0")
varc2 = StringVar()
varc2.set("0")
varc3 = StringVar()
varc3.set("0")
varc4 = StringVar()
varc4.set("0")

# creates check buttons for the choices and modifies its appearance and placement
choice1 = Checkbutton(window, text="Uppercase letters (ABC...XYZ)", bg="#FFF3E2", variable=varc1, onvalue="1", offvalue="0")
choice1.grid(row=6, column=0, sticky='w', padx=10, pady=10)
choice2 = Checkbutton(window, text="Lowercase letters (abc...xyz)", bg="#FFF3E2", variable=varc2, onvalue="1", offvalue="0")
choice2.grid(row=7, column=0, sticky='w', padx=10, pady=10)
choice3 = Checkbutton(window, text="Numbers (012..789)", bg="#FFF3E2", variable=varc3, onvalue="1", offvalue="0")
choice3.grid(row=7, column=1, sticky='e', padx=65, pady=10)
choice4 = Checkbutton(window, text="Special Characters(!@#%^&*)", bg="#FFF3E2", variable=varc4, onvalue="1", offvalue="0")
choice4.grid(row=6, column=1, sticky='e', padx=9, pady=10)

# creates a label, modifies the background, font, and placement of the label in the window
lbl_pass = Label(master=window, text="", font=("Arial", 20), bg="#FFE5CA", bd=3, relief="sunken", width=30, height=4)
lbl_pass.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)

# creates a label, modifies the background, font, and placement of the label in the window
lbl_copy = Label(master=window, text="", bg="#FFF3E2")
lbl_copy.grid(row=12, column=0, columnspan=3, sticky='nsew', padx=10)


# a function that generates the password when there are selected characters and displays an error when nothing is selected,
# uses string module to use its constants
def passgen():
    c1 = string.ascii_uppercase
    c2 = string.ascii_lowercase
    c3 = string.digits
    c4 = string.punctuation
    constant_selected = ""
    random_selected = ""
    pattern_password = ""
    slidelen = slider_var.get()

    if varc1.get() == "1":
        constant_selected += random.choice(c1)
        random_selected += c1

    if varc2.get() == "1":
        constant_selected += random.choice(c2)
        random_selected += c2

    if varc3.get() == "1":
        constant_selected += random.choice(c3)
        random_selected += c3

    if varc4.get() == "1":
        constant_selected += random.choice(c4)
        random_selected += c4

    if constant_selected == "" or random_selected == "":
        lbl_pass.config(text="Error: No character type selected for password generation", fg="#FB021A", font=("Arial", 17))
    else:
        pattern_password += constant_selected
        password_list = list(pattern_password)
        random.shuffle(password_list)
        password = "".join(password_list)
        for a in range(slidelen - len(password)):
            password += random.choice(random_selected)
        lbl_pass.config(text=password, fg="#000000", font=("Source Code Pro", 20, "bold"))
    lbl_copy.config(text="")


# a function that copies the text to clipboard using pyperclip and displays an error when no password is generated
def copy_button():
    text = lbl_pass.cget("text")
    if text:
        pyperclip.copy(text)
        lbl_copy.config(text="Copied to clipboard!", bg="#FFF3E2", fg="#000000", font=("Arial", 10, "bold"))
    else:
        lbl_copy.config(text="Error: No password generated yet", bg="#FFF3E2", fg="#FB021A", font=("Arial", 10, "bold"))


# creates a new frame for the buttons
frm_entry = tk.Frame(master=window)
frm_entry.grid(row=10, column=0, columnspan=3, padx=10, pady=50)
frm_entry.config(bg="#FFF3E2")

# creates a button that generates the password, modifies its appearance and placement
btn_gen = Button(master=frm_entry, text="Generate", command=passgen)
btn_gen.grid(row=10, column=0, sticky='nsew', padx=10)
btn_gen.config(width=25, height=2, bg="#E74646", fg="#FFFFFF", font=("Arial", 10, "bold"))

# creates a button that copies the password, modifies its appearance and placement
btn_copy = Button(master=frm_entry, text="Copy to Clipboard", command=copy_button)
btn_copy.grid(row=11, column=0, sticky='nsew', padx=10, pady=10)
btn_copy.config(width=14, height=2, bg="#FA9884", fg="#000000", font=("Arial", 10, "bold"))


# starts the main event loop
window.mainloop()
