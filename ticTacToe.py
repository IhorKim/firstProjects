from tkinter import *
import random
import time


def stop_game():  # stopping game when we have a winner
    global game_left
    for item in game_left:
        buttons[item].config(state="disabled")


def result(n):  # checking win line
    global game
    if (game[0] == n and game[1] == n and game[2] == n) or (game[3] == n and game[4] == n and game[5] == n) \
            or (game[6] == n and game[7] == n and game[8] == n) or (game[0] == n and game[3] == n and game[6] == n) \
            or (game[1] == n and game[4] == n and game[7] == n) or (game[2] == n and game[5] == n and game[8] == n) \
            or (game[0] == n and game[4] == n and game[8] == n) or (game[2] == n and game[4] == n and game[6] == n):
        return True


def press_button(b):  # logic of moves
    global game
    global game_left
    global move
    game[b] = "X"
    buttons[b].config(text="X", fg="black", state="disabled")
    game_left.remove(b)
    if b == 4 and move == 0:  # if first move is in center
        t = random.choice(game_left)
    elif b != 4 and move == 4:  # if first move is not in center
        t = 4
    if move > 0:
        t = 8 - b
    if t not in game_left:  # catching error at the end of a game
        try:
            t = random.choice(game_left)
        except IndexError:
            label_name["text"] = "Game over!"
            stop_game()
    game[t] = "0"
    time.sleep(0.5)
    buttons[t].config(text="0", fg="black", state="disabled")
    if result("X"):
        label_name["text"] = "You Win!"
        stop_game()
    elif result("0"):
        label_name["text"] = "You lose!"
        stop_game()
    else:
        if len(game_left) > 1:
            game_left.remove(t)
        else:
            label_name["text"] = "Game over!"
            stop_game()
        move += 1


game = [None] * 9
game_left = list(range(9))
move = 0

win = Tk()
win.resizable(False, False)

label_name = Label(text="Tic Tak Toe Game", font=("Arial", 20, "bold"), width=20)
label_name.grid(row=0, column=0, columnspan=3)

buttons = [Button(font=("Arial", 25, "bold"), width=5, height=2, bg="lightblue",
                  command=lambda x=i: press_button(x)) for i in range(9)]  # short syntax for creating the game field using list comprehension

row = 1
col = 0
for i in range(9):  # placing our buttons
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

win.mainloop()
