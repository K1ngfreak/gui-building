import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Pizza')

smallPizza = tk.StringVar()
mediumPizza = tk.StringVar()
largePizza = tk.StringVar()


def small_pizza():
    tk.messagebox.showinfo(title='Amount',
                        message=smallPizza.get())

def medium_pizza():
    tk.messagebox.showinfo(title='Amount',
                        message=mediumPizza.get())

def large_pizza():
    tk.messagebox.showinfo(title='Amount',
                        message=largePizza.get())


ttk.Checkbutton(root,
                text='Small:        20cm - €6.99',
                command=small_pizza,
                variable=smallPizza,
                offvalue=0).pack()

ttk.Checkbutton(root,
                text='Medium:  30cm - €11.99',
                command=medium_pizza,
                variable=mediumPizza,
                offvalue=0).pack()

ttk.Checkbutton(root,
                text='Large:       40cm - €17.99',
                command=large_pizza,
                variable=largePizza,
                offvalue=0).pack()

root.mainloop()