import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.geometry('500x400')
window.title('Pizza')

window.mainloop()


print('Size:')
print('Small:   10 - 20cm - 6.99')
print('Medium:  20 - 30cm - 11.99')
print('Large:   30 - 40cm - 17.99')

price_small = 6.99
price_medium = 11.99
price_large = 17.99

aantal_small = int(input('Aantal small: '))
aantal_medium = int(input('Aantal medium: '))
aantal_large = int(input('Aantal large: '))

ticket_small = float(price_small * aantal_small)
ticket_medium = float(price_medium * aantal_medium)
ticket_large = float(price_large * aantal_large)

receipt = float(ticket_small + ticket_medium + ticket_large)

print(str(receipt) + ' euro')