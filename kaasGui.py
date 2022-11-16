import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Kaas')
window.geometry('300x120')

kaas = ('Emmenthalen', 'Leerdammer', 'Pammigiano Reggiano', 'Goudse kaas', 'Blue de Rochbaron', 'Foume d_Ambert', 'Camembert', 'Mozzarella')

def option1_1():
    pb['value'] += 33.5
    window.geometry('350x120')
    option_button1.configure(text='Er zitten gaten in de kaas', command=option1_2)
    option_button2.configure(text='Er zitten geen gaten in de kaas', command=option1_4)

def option1_2():
    pb['value'] += 33.5
    window.geometry('300x120')
    option_button1.configure(text='De prijs is erg hoog', command=option1_3)
    option_button2.configure(text='De prijs valt mee')

def option1_3():
    pb['value'] += 33
    showinfo(message='Je hebt: Emmenthaler')

def option1_4():
    pb['value'] += 33.5
    option_button1.configure(text='',command=option1_5)

def option2_1():
    pb['value'] += 33.5
    window.geometry('430x120')
    option_button1.configure(text='De kaas heeft blauwe schimmels')
    option_button2.configure(text='De kaas heeft geen blauwe schimmels')

def option2_2():
    pb['value'] += 33.5
    option_button1.configure()
    option_button2.configure()

def option2_3():
    pb['value'] += 33
    option_button1.configure()
    option_button2.configure()

pb = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='determinate',
    length=280
)

option_button1 = ttk.Button(
    window,
    text='de kaas is geel',
    command=option1_1
)

option_button2 = ttk.Button(
    window,
    text='de kaas is niet geel',
    command=option2_1
)

pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

option_button1.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

option_button2.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

window.mainloop()