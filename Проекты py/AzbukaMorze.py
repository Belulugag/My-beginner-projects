from tkinter import *
from winsound import *
tk = Tk()
tk.geometry("500x300")
def code():
    s = ""
    for i in en01.get().upper():
        s += c[i][0] + " "
        l01.config(text = s)
        tk.update()
        PlaySound("sounds/%s" % c[i][1],SND_FILENAME)
c = {"А": [".-", "А.wav"],
    "Б": ["-...", "Б.wav"],
    "В": [".--", "В.wav"],
    "Г": ["--.", "Г.wav"],
    "Д": ["-..", "Д.wav"],
    "Е": [".", "Е.wav"],
    "Ж": ["...-", "Ж.wav"],
    "З": ["--..", "З.wav"],
    "И": ["..", "И.wav"],
    "Й": [".---", "Й.wav"],
    "К": ["-.-", "К.wav"],
    "Л": [".-..", "Л.wav"],
    "М": ["--", "М.wav"],
    "Н": ["-.", "Н.wav"],
    "О": ["---", "О.wav"],
    "П": [".--.", "П.wav"],
    "Р": [".-.", "Р.wav"],
    "С": ["...", "С.wav"],
    "Т": ["-", "Т.wav"],
    "У": ["..-", "У.wav"],
    "Ф": ["..-.", "Ф.wav"],
    "Х": ["....", "Х.wav"],
    "Ц": ["-.-.", "Ц.wav"],
    "Ч": ["---.", "Ч.wav"],
    "Ш": ["----", "Ш.wav"],
    "Щ": ["--.-", "Щ.wav"],
    "Ъ": ["--.--", "Ъ.wav"],
    "Ы": ["-.--", "Ы.wav"],
    "Ь": ["-..-", "Ь.wav"],
    "Э": ["..-..", "Э.wav"],
    "Ю": ["..--", "Ю.wav"],
    "Я": [".-.", "Я.wav"]}
l01 = Label(tk,text = "Введите слово: ",font = "Verdana 27")
l01.pack(pady = 10,padx = 10)
en01 = Entry(tk,font = "Verdana 27")
en01.pack(pady = 10,padx = 10)
btn = Button(tk,text = "Отправить",font = "Verdana 27",command = code)
btn.pack(pady = 10,padx = 10)
tk.mainloop()
