from tkinter import *
tk = Tk()
tk.title("PyBom")
tk.geometry("600x650")

#global
okToPressReturn = True
Day = 0
b = 100
def start(event):

    global okToPressReturn
    if okToPressReturn == False:
        pass
    else:
        strtLabel.pack_forget()
        UpdB()
        UpdD()
        UpUI()
        okToPressReturn = False
def UpUI():
    global b, Day
    if b < 51:
        BNormal.config(image=NN_bomb)
    else:
        BNormal.config(image=Normal_bomb)
        BLabel.config(text="Фитиль: " + str(b))
        DLabel.config(text="День: " + str(Day))
        BNormal.after(100, UpUI)
def UpdB():
    global b
    b -= 1
    if Alive():
        BLabel.after(500,UpdB)
def Alive():
    global b
    if b <= 0:
        strtLabel.config(text = "*Звуки громких взрывов*")
        Normal_bomb.config(image = explosion)
        return False
    else:
        return True
def UpdD():
    global Day
    Day += 1
    if Alive():
        DLabel.after(5000,UpdD)
def stop():
    global b
    if Alive:
        if b <= 30:
            b += 20
        else:
            b -= 20
#labels
strtLabel = Label(tk,text = "Нажмите Enter,\nчтобы начать игру",font = ("White",24))
strtLabel.pack(pady = 10,padx = 10)
BLabel = Label(tk,text = "Фетиль: ",font = ("White",20))
BLabel.pack(pady = 10,padx = 10)
BLabel.config(text = "Фитиль: " + str(b))
DLabel = Label(tk,text = "День: ",font = ("White",20))
DLabel.config(text = "День: " + str(Day))
DLabel.pack(pady = 10,padx = 10)
#images
NN_bomb = PhotoImage(file = "bomb_no.gif")
Normal_bomb = PhotoImage(file = "bomb_normal.gif")
explosion = PhotoImage(file = "bang.gif")
buttonb = Button(tk,text = "Провести сапёрную операцию",command = stop)
buttonb.pack(side = BOTTOM,pady = 10,padx = 10)

BNormal = Label(tk,image = Normal_bomb)
BNormal.pack(pady = 10,padx = 10)
BNNormal = Label(tk,image = NN_bomb)
##BNNormal.pack(pady = 10,padx = 10)
exp = Label(tk,image = explosion)
##exp.pack(pady = 10,padx = 10)

tk.bind("<Return>",start)

tk.mainloop()
