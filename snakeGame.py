import random
from tkinter import *

# constants - easy way for future to change them
WINDOW_SIZE = 600
SPACE_SIZE = 20  # size of one square in pixels
SNAKE_LENGTH = 1
SPEED = 100
COLOR_BODY = "green"
COLOR_HEAD = "blue"
BACKGROUND_COLOR = "black"
FOOD_COLOR = "red"


class Snake:  # creating body
    def __init__(self):
        self.snake_length = SNAKE_LENGTH
        self.coord = [[0, 0]]
        self.squares = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COLOR_BODY)
            self.squares.append(square)


class Food:  # creating apples
    def __init__(self):
        x = random.randrange(0, (WINDOW_SIZE / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randrange(0, (WINDOW_SIZE / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coord = [x, y]
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR)


def move(snake, food):  # determine the coordinates
    for x, y in snake.coord:
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COLOR_BODY)
    x, y = snake.coord[0]

    if direction == "down":
        y += SPACE_SIZE
    elif direction == "up":
        y -= SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coord.insert(0, (x, y))  # insert coordinates of the head
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COLOR_HEAD)
    snake.squares.insert(0, square)

    if x == food.coord[0] and y == food.coord[1]:  # eating an apple
        global score
        score += 1
        label_score.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        x, y = snake.coord[-1]
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BACKGROUND_COLOR)
        del snake.coord[-1]  # rendering our snake
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if food in snake.squares:
        food = Food()

    if check_stop(snake):
        game_over()
    else:
        win.after(SPEED, move, snake, food)  # delay method


def change_direction(new_direction):  # snake movement
    global direction

    if new_direction == "down":
        if direction != "up":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction


def check_stop(snake):  # collisions with borders
    x, y = snake.coord[0]

    if x < 0 or x >= WINDOW_SIZE:
        return True
    elif y < 0 or y >= WINDOW_SIZE:
        return True

    for snake_length in snake.coord[1:]:  # checking collision of head with body
        if x == snake_length[0] and y == snake_length[1]:
            return True


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text="Game Over", font=("Arial", 25), fill="red")
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text="\n\nTry again", font=("Arial", 25), fill="lightblue")


win = Tk()
win.title("Snake Game")
win.resizable(False, False)
win.geometry("650x650")

score = 0
direction = "down"

label_score = Label(win, text="Score: {}".format(score), font=("Arial", 30))
label_score.pack()

canvas = Canvas(win, width=WINDOW_SIZE, height=WINDOW_SIZE, bg=BACKGROUND_COLOR)
canvas.pack()

win.bind("<Down>", lambda event: change_direction("down"))
win.bind("<Up>", lambda event: change_direction("up"))
win.bind("<Left>", lambda event: change_direction("left"))
win.bind("<Right>", lambda event: change_direction("right"))

snake = Snake()
food = Food()
move(snake, food)

win.mainloop()
