# We need to install Tkinter first
# Run the command prompt and type "pip install tk" to install Tkinter library
import tkinter as tk
from tkinter import messagebox


def add_digit(digit):  # inserting numbers in display window from right to left
    value = calculator.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calculator['state'] = tk.NORMAL
    calculator.delete(0, tk.END)
    calculator.insert(tk.END, value + digit)
    calculator['state'] = tk.DISABLED


def add_operation(operation):  # math operations
    value = calculator.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calculator.get()
    calculator['state'] = tk.NORMAL
    calculator.delete(0, tk.END)
    calculator.insert(tk.END, value + operation)
    calculator['state'] = tk.DISABLED


def abs():  # making positive or negative numbers
    value = calculator.get()
    if '-' not in value:
        value = '-' + value
    else:
        value = value[1:]
    calculator['state'] = tk.NORMAL
    calculator.delete(0, tk.END)
    calculator.insert(tk.END, value)
    calculator['state'] = tk.DISABLED


def backspace():  # backspace numbers
    value = calculator.get()
    calculator['state'] = tk.NORMAL
    calculator.delete(0, tk.END)
    if len(value) == 0:
        calculator.insert(0, 0)
    else:
        calculator.insert(tk.END, value[:-1])
    calculator['state'] = tk.DISABLED


def calculate():  # calculating operations
    value = calculator.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calculator['state'] = tk.NORMAL
    calculator.delete(0, tk.END)
    try:  # prevents entering letters and symbols in display + errors
        calculator.insert(tk.END, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Warning', 'Press only numbers')
        calculator.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Warning', 'No zero division')
        calculator.insert(0, 0)
    calculator['state'] = tk.DISABLED


def clear():  # clear the display
    calculator['state'] = tk.NORMAL
    calculator.delete(0, tk.END)
    calculator.insert(0, 0)
    calculator['state'] = tk.DISABLED


def makeButton(digit):  # creating buttons in window
    return tk.Button(text=digit, bd=5, font=('Xenara', 15), command=lambda: add_digit(digit))
    # bd - frame for buttons
    # command - logic for buttons


def makeAbsButton(function):  # making positive or negative number
    return tk.Button(text='+/-', bd=5, font=('Xenara', 15), fg='red', command=lambda: abs())


def makeBackButton(function):
    return tk.Button(text='Bcsp', bd=5, font=('Xenara', 10), fg='red', command=lambda: backspace())


def makeFunctionButton(operation):  # creating buttons in window
    return tk.Button(text=operation, bd=5, font=('Xenara', 15), fg='red', bg='#DAA520',
                     command=lambda: add_operation(operation))


def makeCalcButton(function):  # creating buttons in window
    return tk.Button(text=function, bd=5, font=('Xenara', 15), fg='red', bg='#DAA520', command=calculate)


def makeClearButton(function):  # creating buttons in window
    return tk.Button(text=function, bd=5, font=('Xenara', 15), fg='red', command=clear)


def keyPress(event):  # making entry with keyboard
    print(repr(event.char))  # repr is for "Enter" key
    if event.char.isdigit():  # display numbers
        add_digit(event.char)
    elif event.char in '+-*/':  # display operations
        add_operation(event.char)
    elif event.char == '.':
        add_digit(event.char)
    elif event.char == '\x08':
        backspace()
    elif event.char == '\r':  # rusult with "Enter" key
        calculate()


win = tk.Tk()  # display Tkinter window
win.geometry(f"240x325+100+180")  # size of window
win['bg'] = '#000000'  # window color
win.title('Calculator')

win.bind('<Key>', keyPress)  # making entry with keyboard

calculator = tk.Entry(win, justify=tk.RIGHT, font=('Xenara', 15))  # field for input
calculator.insert(0, 0)
calculator['state'] = tk.DISABLED  # no focus with left mouse button in display
calculator.grid(row=0, column=0, columnspan=5, stick='we', padx=5)

makeButton('1').grid(row=4, column=0, stick='wens', padx=5, pady=5)  # main buttons
makeButton('2').grid(row=4, column=1, stick='wens', padx=5, pady=5)  # stick - place button in whole grid area
makeButton('3').grid(row=4, column=2, stick='wens', padx=5, pady=5)  # padx, pady - interval between buttons
makeButton('4').grid(row=3, column=0, stick='wens', padx=5, pady=5)
makeButton('5').grid(row=3, column=1, stick='wens', padx=5, pady=5)
makeButton('6').grid(row=3, column=2, stick='wens', padx=5, pady=5)
makeButton('7').grid(row=2, column=0, stick='wens', padx=5, pady=5)
makeButton('8').grid(row=2, column=1, stick='wens', padx=5, pady=5)
makeButton('9').grid(row=2, column=2, stick='wens', padx=5, pady=5)
makeButton('0').grid(row=5, column=0, columnspan=2, stick='wens', padx=5, pady=5)
makeButton('.').grid(row=5, column=2, stick='wens', padx=5, pady=5)
makeAbsButton('+/-').grid(row=1, column=2, stick='wens', padx=5, pady=5)
makeBackButton('Bcsp').grid(row=1, column=1, stick='wens', padx=5, pady=5)

makeFunctionButton('+').grid(row=4, column=3, stick='wens', padx=5, pady=5)
makeFunctionButton('-').grid(row=3, column=3, stick='wens', padx=5, pady=5)
makeFunctionButton('/').grid(row=1, column=3, stick='wens', padx=5, pady=5)
makeFunctionButton('*').grid(row=2, column=3, stick='wens', padx=5, pady=5)

makeCalcButton('=').grid(row=5, column=3, stick='wens', padx=5, pady=5)
makeClearButton('C').grid(row=1, column=0, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)  # size of columns
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)  # size of rows
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

win.resizable(False, False)  # not changeable window size

win.mainloop()  # run the Tkinter event loop for buttor clicks or keypresses
