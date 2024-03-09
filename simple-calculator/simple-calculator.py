from tkinter import *
import customtkinter as  CTk
from customtkinter import *

root = CTk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="black")

#commands

equation = ""

def show(value):
    global equation
    equation += value
    label_result.configure(text=equation)
    
def clear():    
    global equation  
    equation = ""
    label_result.configure(text=equation)
    
def calculate():    
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.configure(text=result)           


#buttons

label_result = CTkLabel(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack(padx=50, pady=20)

button = CTkButton(root, text="C", height=80, width=100, font=("arial", 30, "bold"), border_width=1, command=lambda: clear())
button.place(x=10, y=100)

button = CTkButton(root, text="/", height=80, width=100, font=("arial", 30, "bold"), text_color="black", border_width=1, fg_color="#E3E1D9", hover_color="green", command=lambda: show("/"))
button.place(x=150, y=100)

button = CTkButton(root, text="%", height=80, width=100, font=("arial", 30, "bold"), border_width=1, text_color="black", fg_color="#E3E1D9", hover_color="green", command=lambda: show("%"))
button.place(x=290, y=100)

button = CTkButton(root, text="*", height=80, width=100, font=("arial", 30, "bold"), border_width=1, text_color="black", fg_color="#E3E1D9", hover_color="green", command=lambda: show("*"))
button.place(x=430, y=100)


button = CTkButton(root, text="7", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("7"))
button.place(x=10, y=200)

button = CTkButton(root, text="8", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("8"))
button.place(x=150, y=200)

button = CTkButton(root, text="9", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("9"))
button.place(x=290, y=200)

button = CTkButton(root, text="-", height=80, width=100, font=("arial", 30, "bold"), border_width=1, text_color="black", fg_color="#E3E1D9", hover_color="green", command=lambda: show("-"))
button.place(x=430, y=200)


button = CTkButton(root, text="4", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("4"))
button.place(x=10, y=300)

button = CTkButton(root, text="5", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("5"))
button.place(x=150, y=300)

button = CTkButton(root, text="6", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("6"))
button.place(x=290, y=300)

button = CTkButton(root, text="+", height=80, width=100, font=("arial", 30, "bold"), border_width=1, text_color="black", fg_color="#E3E1D9", hover_color="green", command=lambda: show("+"))
button.place(x=430, y=300)


button = CTkButton(root, text="1", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("1"))
button.place(x=10, y=400)

button = CTkButton(root, text="2", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("2"))
button.place(x=150, y=400)

button = CTkButton(root, text="3", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("3"))
button.place(x=290, y=400)

button = CTkButton(root, text="0", height=80, width=240, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="green", command=lambda: show("0"))
button.place(x=10, y=500)


button = CTkButton(root, text=".", height=80, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="black", hover_color="maroon", command=lambda: show("."))
button.place(x=290, y=500)

button = CTkButton(root, text="=", height=180, width=100, font=("arial", 30, "bold"), border_width=1, fg_color="#fe9037", hover_color="green", command=lambda: calculate())
button.place(x=430, y=400)


root.mainloop()