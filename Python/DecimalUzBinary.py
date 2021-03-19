from tkinter import *

gui = Tk()
gui.geometry("320x300")
gui.title("Bināro skaitļu pārveidotājs")
gui.configure(bg="grey")
var = StringVar()
var.set("  🠕 Decimāli skaitļi 🠕\n  🠗 Binārie skaitļi 🠗")


def parversana():
    textbox2.delete("0.0", END)
    x = bin(int(textbox1.get("1.0", END)))
    z = x[2:]
    textbox2.insert(INSERT, z)


textbox1 = Text(gui, height=5, width=25, font=18, bg="Dark gray")
starpteksts = Label(gui, textvariable=var, font=20, bg="gray")
textbox2 = Text(gui, height=5, width=25, font=18, bg="Dark gray")
button = Button(gui, height=5, width=10, font=10, activebackground="#4C4C4C", bg="gray", text="Pārvēršana!",
                command=lambda: parversana())

textbox1.pack()
starpteksts.pack()
textbox2.pack()
button.pack()
gui.mainloop()
