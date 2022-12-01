import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('300x200')
window.title('solicitatie')
















progress = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='determinate',
    length=280
)

button_1 = ttk.Button(
    window,
    text='',
    command=
)

button_2 = ttk.Button(
    window,
    text='',
    command=
)

progress.grid(column=0, row=0, columnspan=2, padx=10 ,pady= 20)

button_1.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

button_2.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)

window.mainloop()