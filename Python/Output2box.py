#def retrieve_input():
#    input = self.myText_Box.get("1.0",END)
from tkinter import *



gui = Tk()
gui.geometry("360x300")
gui.title("Bināro skaitļu pārveidotājs")
var = StringVar()
def retrieve_input():
    return bin(gui.textbox1.get("1.0",END))

textbox1 = Text(gui, height=5, width=25, font=18)
starpteksts = Label(gui, textvariable=var, font=20)
textbox2 = Text(gui, height=5, width=25, font=18)
def printe():
    textbox2_teksts = Label(gui, height=3, width=31, text=retrieve_input())

button = Button(gui, height=5, width=10, font=10, text="Convert!", command=printe())

textbox1.pack()
starpteksts.pack()
var.set("🠕 Decimāli skaitļi 🠕 \n 🠗 Binary 🠗")

textbox2.pack()
button.pack()
gui.mainloop()
