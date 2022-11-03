# Simple hangman word game using Tkinter
import random
from tkinter import *
from tkinter import messagebox

label_word = []
button_letter = []


def line():  # drawing hangman lines
    line_1 = canvas.create_line(100, 600 - 100, 100, 100, width=5)
    line_2 = canvas.create_line(100, 100, 1000 // 3, 100, width=5)
    line_3 = canvas.create_line(1000 // 3, 100, 1000 // 3, 100 * 2, width=5, fill="gold")


def pos_letters():  # creating and placing alphabet letters
    shift_x = shift_y = 0
    count = 0
    for c in range(ord("A"), ord("Z") + 1):  # A - Z big letters only
        btn = Button(text=chr(c), font=("Arial", 18), bg="gray", fg="black", width=2, height=1)
        btn.place(x=700 - 100 * 2 + shift_x, y=75 * 3 - shift_y)
        btn.bind("<Button-1>",
                 lambda event: check_letter(event, word))  # showing right letters when press left mouse button
        button_letter.append(btn)
        shift_x += 50
        count += 1
        if count == 7:  # start new line of buttons
            shift_x = count = 0
            shift_y -= 80


def word():  # taking a word from .txt file
    file = open("wordsForHangmanGame.txt")
    count = 0
    for s in file:  # how many lines in file
        count += 1
    number_word = random.randint(1, count)  # random choosing words
    word = ""
    count = 0
    file = open("wordsForHangmanGame.txt", encoding="utf-8")
    for s in file:
        count += 1
        if count == number_word:  # showing right quantity of letters
            word = s[:len(s) - 1:]
    word = word.upper()
    return word


def position_word(word):  # hiding a word with low dash
    shift = 0
    for i in range(len(word)):
        label_low_dash = Label(win, text="__", font=("Arial", 15), bg="white")
        label_low_dash.place(x=700 - 100 * 2 + shift, y=50 * 3)
        shift += 50
        label_word.append(label_low_dash)


def check_letter(event, word):  # checking the letter in hidden word and display the letter
    letter = event.widget["text"]  # reading the letter
    pos = []
    for i in range(len(word)):
        if word[i] == letter:
            pos.append(i)
    if pos:
        for i in pos:
            label_word[i].config(text="{}".format(word[i]))
        count_letters = 0
        for i in label_word:
            if i["text"].isalpha():
                count_letters += 1
        if count_letters == len(word):
            game_over("win")
    else:
        tries = int(label_tries.cget("text"))
        label_tries.config(text="{}".format(tries - 1))
        if tries == 0:
            game_over("lose")


def game_over(status):
    for btn in button_letter:
        btn.destroy()
    if status == "win":
        messagebox.showinfo(message="Win!")
    else:
        messagebox.showinfo(message="Lose!")


win = Tk()
win.title("Hangman Game")
win.resizable(False, False)
win.geometry("1000x600")

tries = 10
label_text = Label(win, fg="black", bg="brown", text="Tries:", font=("Arial", 15))
label_text.place(x=900, y=0, width=50, height=50)
label_tries = Label(win, text="{}".format(tries), font=("Arial", 15))
label_tries.place(x=950, y=0, width=50, height=50)

canvas = Canvas(win, bg="white", width=1000, height=600)
canvas.place(x=0, y=50)

line()
pos_letters()
word = word()
position_word(word)
print(word)  # show right answer

win.mainloop()
