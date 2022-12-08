import tkinter as tk
from tkinter import ttk

def answerdef():
    progress['value'] += 5
    outcome.append(entryAnswer.get())
    next_question()

def next_question():
    global question
    if entryAnswer == 'M'or entryAnswer == 'm' or entryAnswer == 'man' or entryAnswer == 'Man':
        question += 0.1
    elif entryAnswer == 'F'or entryAnswer == 'f' or entryAnswer == 'vrouw' or entryAnswer == 'Vrouw':
        question += 0.2

    if question == 1:
        question_label.config(text='Hoeveel jaar ervaring heeft u met jongleren?') # 5 jaar
    elif question == 2:
        question_label.config(text='Hoeveel jaar ervaring heeft u met acrobatiek?') # 3 jaar
    elif question == 3:
        question_label.config(text='Welk niveau MBO diploma heeft u?') # niveau 4
    elif question == 4:
        question_label.config(text='Heeft u een geldig vrachtwagen rijbewijs?') # ja
    elif question == 5:
        question_label.config(text='Heeft u een hoge hoed?') # ja
    elif question == 6:
        question_label.config(text='Bent u een man of vrouw?') # man = .1, vrouw = .2
    elif question == 7.1:
        question_label.config(text='Heeft u een snor?') # ja
    elif question == 8.1:
        question_label.config(text='Hoe lang is uw snor in cm?') # 10 cm
    elif question == 7.2:
        question_label.config(text='Draagt u rood krulhaar?') # ja
    elif question == 8.2:
        question_label.config(text='Hoe lang is uw haar in cm') # 20 cm
    elif question == 9:
        question_label.config(text='Hoeveel cm bent u?') # 150 cm
    elif question == 10:
        question_label.config(text='Hoeveel weegt u in kg? (rond af)') # 90 kg
    elif question == 11:
        question_label.config(text='Heeft u het certificaat: “Overleven met gevaarlijk personeel”?') # ja
    question += 1


window = tk.Tk()
window.geometry('300x200')
window.title('solicitatie')

question = 1

outcome = []













progress = ttk.Progressbar(orient='horizontal', mode='determinate', length=280)

label = ttk.Label(text='Beantwoord zo veel mogelijk in cijfers')

question_label = ttk.Label(text='Hoeveel jaar ervaring heeft u met dieren-dressuur?') # 4 jaar

entryAnswer = tk.StringVar()
answer_entry = ttk.Entry(textvariable=entryAnswer)

answer_btn = ttk.Button(text='Submit answer', command=answerdef)


progress.grid(column=0, row=0, columnspan=1, padx=10 ,pady=20)

label.grid(column=0, row=1)

question_label.grid(column=0, row=2)

answer_entry.grid(column=0, row=3)

answer_btn.grid(column=0, row=4)

window.mainloop()