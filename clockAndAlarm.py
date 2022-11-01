# Simple clock and alarm
import time
import winsound
from tkinter import *
from tkinter import messagebox
from time import strftime


def objects():  # display clock values
    label_text = Label(win, font=("Arial", 20), bg="#018ABD", fg="#FFAB41", text="Enter time for alarm hh:mm")
    label_text.place(x=100, y=320, width=350, height=50)

    def validate(P):    # prevents to enter more than 5 characters in entry field
        if len(P) >= 0 and len(P) <= 5:
            return True
        else:
            return False

    vcmd = (win.register(validate), "%P")

    global entry
    entry = Entry(win, font=("Arial", 20), validate="key", validatecommand=vcmd)
    entry.place(x=500, y=320, width=80, height=50)

    but = Button(win, text="Set alarm", command=lambda: alarm())
    but.place(x=650, y=320, width=100, height=50)

    global label_hours
    label_hours = Label(win, font=("Arial", 50), bg="#018ABD", fg="#FFAB41")
    label_hours.place(x=150, y=50, width=150, height=150)
    label_name_hours = Label(win, font=("Arial", 40), bg="#018ABD", fg="#FFAB41", text="hours")
    label_name_hours.place(x=150, y=230, width=150, height=50)

    global label_minutes
    label_minutes = Label(win, font=("Arial", 50), bg="#97CBDC", fg="#FFAB41")
    label_minutes.place(x=350, y=50, width=150, height=150)
    label_name_minutes = Label(win, font=("Arial", 30), bg="#97CBDC", fg="#FFAB41", text="minutes")
    label_name_minutes.place(x=350, y=230, width=150, height=50)

    global label_seconds
    label_seconds = Label(win, font=("Arial", 50), bg="#DDE8F0", fg="#FFAB41")
    label_seconds.place(x=550, y=50, width=150, height=150)
    label_name_seconds = Label(win, font=("Arial", 30), bg="#DDE8F0", fg="#FFAB41", text="seconds")
    label_name_seconds.place(x=550, y=230, width=150, height=50)


def clock():    # placing clock values in Labels
    hours = strftime("%H")
    minutes = strftime("%M")
    seconds = strftime("%S")

    label_hours.config(text="{}".format(hours))
    label_minutes.config(text="{}".format(minutes))
    label_seconds.config(text="{}".format(seconds))

    win.after(1000, clock)


def alarm():    # alarm logic
    set_alarm = entry.get()
    current_time = time.strftime("%H:%M")
    while set_alarm != current_time:
        current_time = time.strftime("%H:%M")
        time.sleep(1)
    if set_alarm == current_time:
        winsound.PlaySound("*", winsound.SND_ASYNC)
        messagebox.showinfo("Alarm")


win = Tk()
win.title("ClockAndAlarm")
win.geometry("850x400")
win.resizable(False, False)

canvas = Canvas(win, bg="#004581", height=400, width=850)
canvas.place(x=0, y=0)

objects()
clock()

win.mainloop()