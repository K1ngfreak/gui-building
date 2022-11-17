import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Pizza')

pizzaSize = ('Small: 20cm - €6.99', 'Medium: 30cm - €11.99', 'Large: 40cm - €17.99')

var = tk.Variable(value=pizzaSize)

listbox = tk.Listbox(
    window,
    listvariable=var,
    height=3,
    selectmode=tk.EXTENDED
)

listbox.pack(expand=True, fill=tk.BOTH)


window.mainloop()




aantal_small = int(input('Aantal small: '))
aantal_medium = int(input('Aantal medium: '))
aantal_large = int(input('Aantal large: '))

ticket_small = float(price_small * aantal_small)
ticket_medium = float(price_medium * aantal_medium)
ticket_large = float(price_large * aantal_large)

receipt = float(ticket_small + ticket_medium + ticket_large)

print(str(receipt) + ' euro')