import tkinter as tk
window = tk.Tk()
window.title("Simple Desktop Application")
window.geometry("700x500")
label = tk.Label(window, text = "Click the button to update this text")
label.grid (row =0, column = 0)
font=('Calibri 15 bold')

def on_click_btn1():
    label["text"] = "You clicked first button"
    
def on_click_btn2():
    label["text"] = "You clicked second button"

field = tk.Entry(window)
field.grid(columnspan=4, ipadx=1)
field.grid(row=1,column=0)

btn1 = tk.Button (window, text = "Button1", command = on_click_btn1)
btn1.grid(row=2, column=0)

btn2 = tk.Button (window, text = "Button2", command = on_click_btn2)
btn2.grid(row=3, column=0)


    
window.mainloop()

