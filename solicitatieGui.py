import tkinter as tk
from tkinter import ttk

def answerdef():
    progress['value'] += 5
    outcome.append(entryAnswer.get())
    next_question()

def next_question():
    global question
    if question == 1:
        question_label.config(text='Hoeveel jaar ervaring heeft u met jongleren?') # 5 jaar
    elif question == 2:
        question_label.config(text='Hoeveel jaar ervaring heeft u met acrobatiek?') # 3 jaar
    elif question == 3:
        question_label.config(text='Welk niveau MBO diploma heeft u?') # niveau 4
    elif question == 4:
        question_label.config(text='Heeft u een geldig vrachtwagen rijbewijs?') # ja


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






            hoed = str(input('Heeft u een hoge hoed? '))
            if hoed == 'ja':
                Geslacht = str(input('Bent u een man of vrouw? '))
                if Geslacht == 'man':
                    snor = str(input('Heeft u een snor? '))
                    if snor == 'ja':
                        lengte_snor = input('Hoeveel cm is uw snor? ')
                        if lengte_snor >= '10':
                            lengte_person = input('Hoeveel cm bent u? ')
                            if lengte_person >= '150':
                                gewicht_persoon = input('Hoeveel weegt u in kg? ')
                                if gewicht_persoon >= '90':
                                    certificaat = str(input('Heeft u het certificaat: “Overleven met gevaarlijk personeel”? '))
                                    if certificaat == 'ja':
                                        print('U kan op solicitatie')
                                    else:
                                        print('U kwalificeert niet voor de baan')
                                else:
                                    print('U kwalificeert niet voor de baan')
                            else:
                                print('U kwalificeert niet voor de baan')
                        else:
                            print('U kwalificeert niet voor de baan')
                    else:
                        print('U kwalificeert niet voor de baan')
                elif Geslacht == 'vrouw':
                    krulhaar = str(input('Draagt u rood krulhaar? '))
                    if krulhaar == 'ja':
                        lengte_krulhaar = input('Hoelang is uw haar? ')
                        if lengte_krulhaar > '20':
                            lengte_person = input('Hoeveel cm bent u? ')
                            if lengte_person >= '150':
                                gewicht_persoon = input('Hoeveel weegt u in kg? ')
                                if gewicht_persoon >= '90':
                                    certificaat = str(input('Heeft u het certificaat: “Overleven met gevaarlijk personeel”? '))
                                    if certificaat == 'ja':

