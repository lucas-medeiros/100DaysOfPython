# @author   Lucas Cardoso de Medeiros
# @since    05/07/2022
# @version  1.0

# Password Generator GUI

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please, don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Information entered:\nEmail: {email}\n"
                                               f"Password: {password}\nIs it ok to save?")
        if is_ok:
            try:
                file = open(file="data.json", mode="r")
                data = json.load(file)  # Read old data
            except FileNotFoundError:
                file = open(file="data.json", mode="w")
                data = new_data
            else:
                data.update(new_data)  # Update old data
            finally:
                with open(file="data.json", mode="w") as file:
                    json.dump(data, file, indent=4)  # Write new data
                entry_website.delete(0, END)
                entry_email.config(text=DEFAULT_EMAIL)
                entry_password.delete(0, END)


# ------------------------ SEARCH PASSWORD INFO --------------------------- #
def search_password():
    website = entry_website.get()
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", justify="right", bg="white", fg="black")
label_website.grid(column=0, row=1)

entry_website = Entry(window, bg="white", fg="black", highlightthickness=0)
entry_website.grid(column=1, row=1, columnspan=1, sticky="EW")
entry_website.focus()

button_search = Button(text="Search", command=search_password, highlightthickness=0, bg="white")
button_search.grid(column=2, row=1, sticky="EW")

label_email = Label(text="Email/Username:", justify="right", bg="white", fg="black")
label_email.grid(column=0, row=2, )

entry_email = Entry(window, bg="white", fg="black", highlightthickness=0)
entry_email.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email.insert(0, DEFAULT_EMAIL)

label_password = Label(text="Password:", justify="right", bg="white", fg="black")
label_password.grid(column=0, row=3)

entry_password = Entry(window, bg="white", fg="black", highlightthickness=0)
entry_password.grid(column=1, row=3, columnspan=1, sticky="EW")

button_generate = Button(text="Generate Password", command=generate_password, highlightthickness=0, bg="white")
button_generate.grid(column=2, row=3, sticky="EW")

button_add = Button(text="Add", command=save_password, highlightthickness=0, bg="white")
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
