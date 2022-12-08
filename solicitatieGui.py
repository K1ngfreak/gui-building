import tkinter as tk
from tkinter import ttk


def next_question():
    global outcome
    global question
    progress['value'] += 8

    if question == 1:
        if entryAnswerInt.get() < 4:
            outcome = 'no'
        question_label_1.config(text='Hoeveel jaar ervaring heeft u met jongleren?') # 5 jaar
    elif question == 2:
        if entryAnswerInt.get() < 5:
            outcome = 'no'
        question_label_1.config(text='Hoeveel jaar ervaring heeft u met acrobatiek?') # 3 jaar
    elif question == 3:
        if entryAnswerInt.get() < 3:
            outcome = 'no'
        question_label_1.config(text='Welk niveau MBO diploma heeft u?') # niveau 4
    elif question == 4:
        if entryAnswerInt.get() < 4:
            outcome = 'no'
        question_label_1.config(text='Heeft u een geldig vrachtwagen rijbewijs?') # ja
        answer_entry.config(textvariable=entryAnswerString)
    elif question == 5:
        if entryAnswerString.get() == 'nee' or entryAnswerString.get() == 'N' or entryAnswerString.get() == 'n' or entryAnswerString.get() == 'Nee':
            outcome = 'no'
        question_label_1.config(text='Heeft u een hoge hoed?') # ja
    elif question == 6:
        if entryAnswerString.get() == 'nee' or entryAnswerString.get() == 'N' or entryAnswerString.get() == 'n' or entryAnswerString.get() == 'Nee':
            outcome = 'No'
        question_label_1.config(text='Indien u een man bent (anders ja):')
        question_label_2.config(text='Heeft u een snor?') # ja
    elif question == 7:
        if entryAnswerString.get() == 'nee' or entryAnswerString.get() == 'N' or entryAnswerString.get() == 'n' or entryAnswerString.get() == 'Nee':
            outcome = 'No'
        question_label_1.config(text='Indien U een man bent (anders 100):')
        question_label_2.config(text='Hoe lang is uw snor in cm?') # 10 cm
        answer_entry.config(textvariable=entryAnswerInt)
    elif question == 8:
        if entryAnswerInt.get() < 10:
            outcome = 'No'
        question_label_1.config(text='Indien u een vrouw bent (anders ja):')
        question_label_2.config(text='Draagt u rood krulhaar?') # ja
        answer_entry.config(textvariable=entryAnswerString)
    elif question == 9:
        if entryAnswerString.get() == 'nee' or entryAnswerString.get() == 'N' or entryAnswerString.get() == 'n' or entryAnswerString.get() == 'Nee':
            outcome = 'No'
        question_label_1.config(text='Indien u een vrouw bent (anders 100):')
        question_label_2.config(text='Hoe lang is uw haar in cm') # 20 cm
        answer_entry.config(textvariable=entryAnswerInt)
    elif question == 10:
        if entryAnswerInt.get() < 20:
            outcome = 'No'
        question_label_1.config(text='Hoeveel cm bent u?') # 150 cm
        question_label_2.config(text='')
    elif question == 11:
        if entryAnswerInt.get() < 150:
            outcome = 'No'
        question_label_1.config(text='Hoeveel weegt u in kg? (rond af)') # 90 kg
    elif question == 12:
        if entryAnswerInt.get() < 90:
            outcome = 'No'
        question_label_1.config(text='Heeft u het certificaat:') # ja
        question_label_2.config(text='“Overleven met gevaarlijk personeel”?')
        answer_entry.config(textvariable=entryAnswerString)
    elif question == 13:
        if entryAnswerString.get() == 'nee' or entryAnswerString.get() == 'N' or entryAnswerString.get() == 'n' or entryAnswerString.get() == 'Nee':
            outcome = 'No'
        if outcome == 'Yes':
            print
        elif outcome == 'No':
            print  
    question += 1
    


window = tk.Tk()
window.geometry('300x200')
window.title('solicitatie')

question = 1

outcome = 'Yes'


progress = ttk.Progressbar(orient='horizontal', mode='determinate', length=280)

label = ttk.Label(text='Beantwoord zo veel mogelijk in cijfers')

question_label_1 = ttk.Label(text='Hoeveel jaar ervaring heeft u met dieren-dressuur?') # 4 jaar
question_label_2 = ttk.Label(text='')

entryAnswerString = tk.StringVar()
entryAnswerInt = tk.IntVar()
answer_entry = ttk.Entry(textvariable=entryAnswerInt)

answer_btn = ttk.Button(text='Submit answer', command=next_question)


progress.grid(column=0, row=0, columnspan=1, padx=10 ,pady=20)

label.grid(column=0, row=1)

question_label_1.grid(column=0, row=2)

question_label_2.grid(column=0, row=3)

answer_entry.grid(column=0, row=4)

answer_btn.grid(column=0, row=5)

window.mainloop()