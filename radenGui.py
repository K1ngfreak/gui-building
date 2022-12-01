import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

def continueDef():
    messageLabel1.destroy()
    messageLabel2.destroy()
    messageLabel3.destroy()
    continueBtn.destroy()
    randomNumber()

def randomNumber():
    global rounds
    global numberToGuess
    rounds += 1
    if rounds == 21:
        finished()
    numberToGuess = int(random.randint(1,1000))
    game()

def game():
    messageLabel4.pack_forget()
    messageLabel5.pack_forget()
    retryBtn.pack_forget()
    stopBtn.pack_forget()
    messageLabelHigher.pack_forget()
    messageLabelLower.pack_forget()
    messageLabelWarm.pack_forget()
    messageLabelCold.pack_forget()
    againBtn.pack_forget()
    global guess
    guess += 1
    if guess == 11:
        restart()
    counter.config(text='round: ' + str(rounds) + ', guess: ' + str(guess))
    counter.pack()
    entryGuess.pack()
    Guesscommit.pack()

def Guess():
    entryGuess.pack_forget()
    Guesscommit.pack_forget()
    global numberToGuess
    global points
    number = numberToGuess - myGuess.get()
    if myGuess.get() == numberToGuess:
        points += 1
        restart()

    elif myGuess.get() < numberToGuess:
        messageLabelHigher.pack()
        if abs(number) < 51:
            messageLabelWarm.pack()
        elif abs(number) > 50:
            messageLabelCold.pack()
        againBtn.pack()

    elif myGuess.get() > numberToGuess:
        messageLabelLower.pack()
        if abs(number) < 51:
            messageLabelWarm.pack()
        elif abs(number) > 50:
            messageLabelCold.pack()
        againBtn.pack()

def restart():
    global guess
    guess = 0
    messageLabel4.config(text='you have ' + str(points) + ' out of the ' + str(rounds) + ' points')
    messageLabel4.pack()
    messageLabel5.pack()
    retryBtn.pack()
    stopBtn.pack()

def finished():
    messageLabel4.config(text='you have ' + str(points) + ' out of the ' + str(rounds) + ' points')
    messageLabel4.pack()
    stopBtn.pack()

window = tk.Tk()
window.title('Raden')
window.geometry('400x200')

# background point and round counter
points = 0
rounds = 0
guess = 0

# rules layed out
messageLabel1 = ttk.Label(text='You need to guess a random number between 1 and 1000')
messageLabel1.pack()

messageLabel2 = ttk.Label(text='There are 20 rounds with 10 guesses each round')
messageLabel2.pack()

messageLabel3 = ttk.Label(text='If you guess closer than 50 to the number you need to guess it\'s warm')
messageLabel3.pack()

continueBtn = ttk.Button(text='continue', command=continueDef)
continueBtn.pack()

# round and geuss counter
counter = ttk.Label(text='round: ' + str(rounds) + ', guess: ' + str(guess))

# restart options
messageLabel4 = ttk.Label(text='you have ' + str(points) + ' out of the ' + str(rounds) + ' points')

messageLabel5 = ttk.Label(text='Do you want to try again?')

retryBtn = ttk.Button(text='Retry', command=randomNumber)

stopBtn = ttk.Button(text='Stop', command=quit)

# choice input and program output
myGuess = tk.IntVar()

entryGuess = ttk.Entry(textvariable=myGuess)

Guesscommit = ttk.Button(text='guess', command=Guess)

messageLabelHigher = ttk.Label(text='The number you need to guess is higher')

messageLabelLower = ttk.Label(text='The number you need to guess is lower')

messageLabelWarm = ttk.Label(text='You are warm')

messageLabelCold = ttk.Label(text='You are cold')

againBtn = ttk.Button(text='Guess again', command=game)


window.mainloop()