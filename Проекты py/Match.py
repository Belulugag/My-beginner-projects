from tkinter import *
from tkinter import ttk
from random import *
from random import randint,choice
#globals
time = 30
score = 0
#Main functions
def generate():
    num = randint(2,6)
    example = ""
    valid = False
    while not valid:
        example = ""
        for i in range(num-1):
            example += str(randint(0,2))
            example += choice(["-","+","*","/","//"])
        example += str(randint(0,2))
        try:
            sovled = eval(example)
            if isinstance(sovled,int):
                valid = True
        except:
            pass
    return example
def start():
    global time,score
    showAll()
    time = 30
    score = 0
    sLabel["text"] = "Score:" + str(score)
    tLabel["text"] = "Time:" + str(time)
    PrimerLabel["text"] = generate()
    updtime()
def hideAll():
    aLabel.grid_remove()
    Enter.grid_remove()
    skip.grid_remove()
    tLabel.grid_remove()
    PrimerLabel.grid_remove()
    for button in buttons:
        button.grid_remove()
    tk["bg"] = "Black"
    StrtButton.place(x = 80,y = 350)
def showAll():
    aLabel.grid()
    Enter.grid()
    skip.grid()
    PrimerLabel.grid()
    tLabel.grid()
    for button in buttons:
        button.grid()
    tk["bg"] = "White"
    StrtButton.place_forget()
def add(i):
    if i != "-" and len(aLabel["text"]) < 30 or aLabel["text"] == "":              
        aLabel["text"] = aLabel["text"] + i
def delete():
    aLabel["text"] = aLabel["text"][:-1]
def updtime():
    global time
    time -= 1
    tLabel["text"] = "Time: " + str(time)
    tk.after(1000, updtime)
    if time < 0:
        hideAll()
    else:
        pass
#control
def Keysc(event):
    if event.char.isdigit() or event.char == "-":
        addDigit(event.char)
def sPrimer():
    global score
    PrimerLabel["text"] = generate()
    aLabel["text"] = ""
    score -= 1
    sLabel["text"] = "Score:" + str(score)
#check answer
def check():
    global score
    try:
        if eval(PrimerLabel["text"]) == int(aLabel["text"]):
            aLabel["text"] = ""
            PrimerLabel["text"] = generate()
            score +=5
            sLabel["text"] = "Score:" + str(score)
        else:

            pass
    except ValueError:
        pass
    except:
        pass
tk = Tk()
tk.title("Решай примеры чтобы решить.")
tk.geometry("468x895")
#tk.resizable(False,False)
PrimerLabel = Label(tk,width = 5,height = 3,text = generate(),bg = "white",font = "Arial 20")
PrimerLabel.grid(columnspan = 4,row = 1,sticky = "ew")
buttons = ["1","2","3",
           "4","5","6",
           "7","8","9",
           "0","-","Delete"]
cc = 0
cr = 2
n = 10.5
for i in range(len(buttons)):
    if i != 11:
        buttons[i] = Button(tk,width = 5,height = 3,
                           bg = "White",text = buttons[i],font = "Arial 20",
                            command = lambda x = buttons[i]: add(x))
    elif i == 11:
        buttons[i] = Button(tk,width = 5,height = 3,
                           bg = "White",text = buttons[i],font = "Arial 20",
                            command = delete)
    buttons[i].grid(column = cc,row = cr)
    cc += 1
    if cc > 2:
        cc = 0
        cr +=1

#time/score
tLabel = Label(tk,width = 5,height = 3,bg = "white",font = "Arial 20")
tLabel.grid(column = 0,columnspan = 2,row = 0,sticky = "ew")
sLabel = Label(tk,width = 5,height = 3,bg = "white",font = "Arial 20")
sLabel.grid(column = 3,columnspan = 2,row = 0,sticky = "ew")
##Result = Label
#addetionally buttons
skip = Button(tk,width = 12,height = 3,
                       bg = "White",text = "Skip",font = "Arial 20",command = sPrimer)
skip.grid(row = 5,column = 3,sticky = "ewns")
Enter = Button(tk,width = 12,height = 10,
                       bg = "White",text = "Enter",font = "Arial 20",command = check)
Enter.grid(row = 2,column = 3,rowspan = 3,sticky = "ewns")
StrtButton = Button(tk,height = 3,width = 24,bg = "White",text = "START",command = start)
#our answer
aLabel = Label(tk,width = 5,height = 3,bg = "white",font = "Arial 20")
aLabel.grid(columnspan = 4,row = 8,sticky = "ew")
generate()
hideAll()
tk.bind("<Enter>",lambda event: check())
tk.bind("<BackSpace>",lambda event: delete())
tk.bind("<space>",lambda event: sPrimer())
tk.bind("<Key>", Keysc)
tk.mainloop()
