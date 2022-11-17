import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title('Pizza')

# pizza's
smallPizza = tk.IntVar()
mediumPizza = tk.IntVar()
largePizza = tk.IntVar()

# eindscherm
def ordered():
    payment = 6.99 * smallPizza.get() + 11.99 * mediumPizza.get() + 17.99 * largePizza.get()
    msg = f'That will be: €{round(payment, 2)}'
    showinfo(
        title='Information',
        message=msg
    )

orders = ttk.Frame(root)
orders.pack(padx=10, pady=10, fill='x', expand=True)

# size small
small_label = ttk.Label(orders, text='Small - 20cm - €6.99:')
small_label.pack(fill='x', expand=True)

small_entry = ttk.Entry(orders, textvariable=smallPizza)
small_entry.pack(fill='x', expand=True)

# size medium
medium_label = ttk.Label(orders, text='Medium:  20 - 30cm - €11.99:')
medium_label.pack(fill='x', expand=True)

medium_entry = ttk.Entry(orders, textvariable=mediumPizza)
medium_entry.pack(fill='x', expand=True)

# size large
large_label = ttk.Label(orders, text='Large:   30 - 40cm - €17.99:')
large_label.pack(fill='x', expand=True)

large_entry = ttk.Entry(orders, textvariable=largePizza)
large_entry.pack(fill='x', expand=True)

# ordering
order_button = ttk.Button(orders, text='order', command=ordered)
order_button.pack(fill='x', expand=True, pady=10)


root.mainloop()