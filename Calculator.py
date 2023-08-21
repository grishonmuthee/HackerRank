#!/usr/bin/env python3

import tkinter as tk
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("700x500")
label1 = tk.Label(window, text = "Enter the Digits Below")
label1.grid (row =0, column = 0)
font=('Calibri 15 bold')

numbers = ""
equation = ""
def press(num):
    global numbers
    numbers = numbers + str(num)
    field.insert(tk.END, num)
    # equation.set(numbers)

def equals():
    try:
        number = field.get()
        result = str(eval(number))
        field.delete(0, tk.END)
        field.insert(tk.END, result)
    except Exception as e:
        field.delete(0, tk.END)
        field.insert( tk.END, 'Error')
        
field = tk.Entry(window)
field.grid(columnspan=4, ipadx=1)
field.grid(row=1,column=0)

btn1 = tk.Button (window, text = "1", command=lambda: press(1))
btn1.grid(row=2, column=1)

btn2 = tk.Button (window, text = "2", command=lambda: press(2))
btn2.grid(row=2, column=2)

btn3 = tk.Button (window, text = "3", command=lambda: press(3))
btn3.grid(row=2, column=3)

btnplus = tk.Button (window, text = "+", command = lambda: press('+'))
btnplus.grid(row = 2, column = 4)

btn4 = tk.Button (window, text = "4", command=lambda: press(4))
btn4.grid(row=3, column=1)

btn5 = tk.Button (window, text = "5", command=lambda: press(5))
btn5.grid(row=3, column=2)

btn6 = tk.Button (window, text = "6", command=lambda: press(6))
btn6.grid(row=3, column=3)

btnminus = tk.Button (window, text = "-", command = lambda: press('-'))
btnminus.grid(row = 3, column = 4)

btn7 = tk.Button (window, text = "7", command=lambda: press(7))
btn7.grid(row=4, column=1)

btn8 = tk.Button (window, text = "8", command=lambda: press(8))
btn8.grid(row=4, column=2)

btn9 = tk.Button (window, text = "9", command=lambda: press(9))
btn9.grid(row=4, column=3)

btntimes = tk.Button (window, text = "*", command = lambda: press('*'))
btntimes.grid(row = 4, column = 4)

btndivide = tk.Button (window, text = "/", command = lambda: press('/'))
btndivide.grid(row = 5, column = 4)

btn0 = tk.Button (window, text = "0", command=lambda: press(0))
btn0.grid(row=5, column=1)

btnpoint = tk.Button (window, text = ".", command=lambda: press('.'))
btnpoint.grid(row=5, column=2)


btnclear = tk.Button (window, text = "Clear", command=lambda: field.delete(0, tk.END))
btnclear.grid(row=10, column=1)

btnc = tk.Button (window, text = "C", command=lambda: field.delete(-1))
btnc.grid(row=6, column=1)

btnexit = tk.Button (window, text = "Exit", command=lambda: press())
btnexit.grid(row=10, column=2)

btnequals = tk.Button (window, text = "=", command= equals)
btnequals.grid(row=6, column=4)

    
window.mainloop()

