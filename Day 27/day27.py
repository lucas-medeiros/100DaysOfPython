# @author   Lucas Cardoso de Medeiros
# @since    01/07/2022
# @version  1.0

# Tkinter GUI

from tkinter import *


def convert():
    label_num.config(text=f"{(float(entry_miles.get()) * 1.609)}")


window = Tk()
window.title("Km Converter")
window.minsize(width=100, height=100)
window.config(padx=25, pady=25)


label_equals = Label(text="is equal to: ", justify="center", pady=10)
label_equals.grid(column=0, row=1)

entry_miles = Entry(width=15)
entry_miles.grid(column=1, row=0)

label_num = Label(text="0", justify="center", pady=5)
label_num.grid(column=1, row=1)

label_mi = Label(text="Miles", justify="center", pady=5)
label_mi.grid(column=2, row=0)

label_km = Label(text="Km", justify="center", pady=5)
label_km.grid(column=2, row=1)

button_calculate = Button(text="Calculate", command=convert)
button_calculate.grid(column=1, row=2)

window.mainloop()
