import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

def continueDef():
    messageLabel1.destroy()
    messageLabel2.destroy()
    continueBtn.destroy()

def game():
    global round
    global guess

window = tk.Tk()
window.title('Raden')
window.geometry('300x200')

# rules layed out
messageLabel1 = ttk.Label(text='Er is een random getal tussen de 1 en de 1000')
messageLabel1.pack()

messageLabel2 = ttk.Label(text='Er zijn 20 rondes en je krijgt 10 kansen per ronde')
messageLabel2.pack()

continueBtn = ttk.Button(text='continue', command=continueDef)
continueBtn.pack()

# background point and round counter
points = 0
round = 0
guess = 0





window.mainloop()