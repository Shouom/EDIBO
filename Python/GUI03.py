from tkinter import *

dec=0

gui = Tk()
gui.geometry("360x300")
gui.title("Bināro skaitļu pārveidotājs")
var = StringVar()
def panemt_decimalskaitli():
        input=textbox1.get("1.0",'end-1c')

textbox1 = Text(gui, height=5, width=25, font=18)
starpteksts = Label(gui, textvariable=var, font=20)
textbox2 = Text(gui, height=5, width=25, font=18,)
def printe():
    textbox2_teksts = Label(gui, height=3, width=31, text=(panemt_decimalskaitli))
button = Button(gui, height=5, width=10, font=10, text="Pārvērst!", command=printe)

textbox1.pack()
starpteksts.pack()
var.set("🠕 Decimāli skaitļi 🠕 \n 🠗 Bināri skaitļi 🠗")

textbox2.pack()
button.pack()
gui.mainloop()
