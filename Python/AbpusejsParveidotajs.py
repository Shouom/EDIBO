def parversana2():
    textbox1.delete("0.0", END)
    x = int(bin(textbox2.get("1.0", END)))
    z = x[2:]
    textbox1.insert(INSERT, z)


def parversana():
    textbox2.delete("0.0", END)
    x = bin(int(textbox1.get("1.0", END)))
    z = x[2:]
    textbox2.insert(INSERT, z