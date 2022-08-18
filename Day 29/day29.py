# @author   Lucas Cardoso de Medeiros
# @since    05/07/2022
# @version  1.0

# Password Generator GUI

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


FONT = ("Arial", 15, "normal")
DEFAULT_EMAIL = "lucascarmed@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = random_letters + random_symbols + random_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if input_website.get() == "" or input_password.get() == "" or input_password.get() == "":
        messagebox.showerror(title="Oops", message="Please, don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=input_website.get(),
                                       message=f"Information entered:\n Email: {input_email.get()}\n"
                                               f"Password: {input_password.get()}\nIs it ok to save?")

        if is_ok:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{input_website.get()} | {input_password.get()} | {input_password.get()}\n")
            input_website.delete(0, END)
            input_email.config(text=DEFAULT_EMAIL)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", justify="center", pady=5, font=FONT, bg="white", fg="black")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:", justify="center", font=FONT, bg="white", fg="black")
label_email.grid(column=0, row=2)

label_email = Label(text="Password:", justify="center", font=FONT, bg="white", fg="black")
label_email.grid(column=0, row=3)

input_website = Entry(window, bg="white", fg="black", highlightthickness=0, width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email = Entry(window, bg="white", fg="black", highlightthickness=0, width=35)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, DEFAULT_EMAIL)

input_password = Entry(window, bg="white", fg="black", highlightthickness=0, width=21)
input_password.grid(column=1, row=3, columnspan=1)

button_generate = Button(text="Generate Password", command=generate_password, highlightthickness=0, bg="white")
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", command=save_password, highlightthickness=0, width=36)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
