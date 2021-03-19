from tkinter import *
import random
#value = random.randint(1,10)
#print(value)
x = random.randint(1,20000)
y = random.randint(1,20000)
while x < y:
	print(x)
	print(y)
	x += 1
root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set(x)
var.set(y)
label.pack()
root.mainloop()