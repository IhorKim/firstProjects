import random
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Rock Paper Scissors")
win.geometry("600x400")
win.resizable(False, False)
win['bg'] = 'pink'

wins = 0
losses = 0
ties = 0


def play_rock():  # main logic of the game if you choose rock
    value = random.randint(1, 3)
    if value == 1:
        label_comp.config(text="Rock")
        global ties
        ties += 1
        label_ties.config(text="{}".format(ties))
        messagebox.showinfo(message="Tie!")
    elif value == 2:
        label_comp.config(text="Paper")
        global losses
        losses += 1
        label_losses.config(text="{}".format(losses))
        messagebox.showinfo(message="Lose!")
    else:
        label_comp.config(text="Scissors")
        global wins
        wins += 1
        label_wins.config(text="{}".format(wins))
        messagebox.showinfo(message="Win!")


def play_paper():  # main logic of the game if you choose paper
    value = random.randint(1, 3)
    if value == 1:
        label_comp.config(text="Rock")
        global wins
        wins += 1
        label_wins.config(text="{}".format(wins))
        messagebox.showinfo(message="Win!")
    elif value == 2:
        label_comp.config(text="Paper")
        global ties
        ties += 1
        label_ties.config(text="{}".format(ties))
        messagebox.showinfo(message="Tie!")
    else:
        label_comp.config(text="Scissors")
        global losses
        losses += 1
        label_losses.config(text="{}".format(losses))
        messagebox.showinfo(message="Lose!")


def play_scissors():  # main logic of the game if you choose scissors
    value = random.randint(1, 3)
    if value == 1:
        label_comp.config(text="Rock")
        global losses
        losses += 1
        label_losses.config(text="{}".format(losses))
        messagebox.showinfo(message="Lose!")
    elif value == 2:
        label_comp.config(text="Paper")
        global wins
        wins += 1
        label_wins.config(text="{}".format(wins))
        messagebox.showinfo(message="Win!")
    else:
        label_comp.config(text="Scissors")
        global ties
        ties += 1
        label_ties.config(text="{}".format(ties))
        messagebox.showinfo(message="Tie!")


label_comp = Label(win, text="", font=("Arial", 35), bg="purple", fg="white")
label_comp.place(x=200, y=150, width=200, height=100)

label_wins = Label(win, text="", font=("Arial", 20), bg="gold", fg="black")
label_wins.place(x=100, y=325, width=50, height=40)

label_losses = Label(win, text="", font=("Arial", 20), bg="brown", fg="black")
label_losses.place(x=275, y=325, width=50, height=40)

label_ties = Label(win, text="", font=("Arial", 20), bg="silver", fg="black")
label_ties.place(x=450, y=325, width=50, height=40)

rock = Button(win, text="Rock", font=("Arial", 20), bg="gray", fg="black", command=lambda: play_rock())
rock.place(x=50, y=50, width=150, height=75)

paper = Button(win, text="Paper", font=("Arial", 20), bg="#F5F5DC", fg="black", command=lambda: play_paper())
paper.place(x=225, y=50, width=150, height=75)

scissors = Button(win, text="Scissors", font=("Arial", 20), bg="#A8A9AD", fg="black", command=lambda: play_scissors())
scissors.place(x=400, y=50, width=150, height=75)

label_text_wins = Label(win, text="Wins:", font=("Arial", 20), bg="gold", fg="black")
label_text_wins.place(x=50, y=275, width=150, height=40)

label_text_losses = Label(win, text="Losses:", font=("Arial", 20), bg="brown", fg="black")
label_text_losses.place(x=225, y=275, width=150, height=40)

label_text_ties = Label(win, text="Ties:", font=("Arial", 20), bg="silver", fg="black")
label_text_ties.place(x=400, y=275, width=150, height=40)

win.mainloop()

