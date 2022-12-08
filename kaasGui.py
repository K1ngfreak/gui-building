import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Kaas')
window.geometry('300x120')

def option1_1():
    pb['value'] += 33.5
    window.geometry('350x120')
    option_button1.configure(text='Er zitten gaten in de kaas', command=option1_2_1)
    option_button2.configure(text='Er zitten geen gaten in de kaas', command=option1_2_2)

def option1_2_1():
    pb['value'] += 33.5
    window.geometry('300x120')
    option_button1.configure(text='De prijs is erg hoog', command=option1_3_1)
    option_button2.configure(text='De prijs valt mee', command=option1_3_2)

def option1_2_2():
    pb['value'] += 33.5
    window.geometry('300x120')
    option_button1.configure(text='De kaas is erg hard', command=option1_3_3)
    option_button2.configure(text='De kaas is niet hard', command=option1_3_4)

def option1_3_1():
    pb['value'] += 33
    showinfo(message='Je hebt: Emmenthaler')

def option1_3_2():
    pb['value'] += 33
    showinfo(message='Je hebt: Leerdammer')

def option1_3_3():
    pb['value'] += 33
    showinfo(message='Je hebt: Pammigiano Reggiano')

def option1_3_4():
    pb['value'] += 33
    showinfo(message='Je hebt: Goudse kaas')

def option2_1():
    pb['value'] += 33.5
    window.geometry('430x120')
    option_button1.configure(text='De kaas heeft blauwe schimmels', command=option2_2_1)
    option_button2.configure(text='De kaas heeft geen blauwe schimmels', command=option2_2_2)

def option2_2_1():
    pb['value'] += 33.5
    window.geometry('310x120')
    option_button1.configure(text='De kaas heeft een korst', command=option2_3_1)
    option_button2.configure(text='De kaas heeft geen korst', command=option2_3_2)

def option2_2_2():
    pb['value'] += 33
    window.geometry('310x120')
    option_button1.configure(text='De kaas heeft een korst', command=option2_3_3)
    option_button2.configure(text='De kaas heeft geen korst', command=option2_3_4)

def option2_3_1():
    pb['value'] += 33
    showinfo(message='Je hebt: Bleu de Rochbaron')

def option2_3_2():
    pb['value'] += 33
    showinfo(message='Je hebt: Foume d_Ambert')

def option2_3_3():
    pb['value'] += 33
    showinfo(message='Je hebt: Camembert')

def option2_3_4():
    pb['value'] += 33
    showinfo(message='Je hebt: mozzarella')


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