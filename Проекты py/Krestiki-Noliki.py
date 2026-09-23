from tkinter import *
import sys

def reset_game():
    global a, c, game_over_label
    a = [0] * 9
    c = 0
    cs.delete("all")
    cs.create_line(50, 120, 250, 120, fill="white")
    cs.create_line(50, 180, 250, 180, fill="white")
    cs.create_line(120, 50, 120, 250, fill="white")
    cs.create_line(180, 50, 180, 250, fill="white")
    if game_over_label:
        game_over_label.destroy()
        game_over_label = None

def check_win():
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]
    for i, j, k in wins:
        if a[i] == a[j] == a[k] != 0:
            return a[i]
    return 0

def show_game_over(winner):
    global game_over_label
    if winner == 1:
        message = "Игрок 1 (X) выиграл!"
    elif winner == 2:
        message = "Игрок 2 (O) выиграл!"
    else:
        message = "Ничья!"

    game_over_label = Label(tk, text=message, font=("Arial", 20), fg="yellow", bg="black")
    game_over_label.place(relx=0.5, rely=0.05, anchor=CENTER)

def draw_f(posx, posy, player):
    global c, a, game_over_label

    if game_over_label:
        return

    cell_num = -1
    if 50 <= posx <= 120:
        if 50 <= posy <= 120: cell_num = 0
        elif 120 <= posy <= 180: cell_num = 3
        elif 180 <= posy <= 250: cell_num = 6
    elif 120 <= posx <= 180:
        if 50 <= posy <= 120: cell_num = 1
        elif 120 <= posy <= 180: cell_num = 4
        elif 180 <= posy <= 250: cell_num = 7
    elif 180 <= posx <= 250:
        if 50 <= posy <= 120: cell_num = 2
        elif 120 <= posy <= 180: cell_num = 5
        elif 180 <= posy <= 250: cell_num = 8

    if 0 <= cell_num < 9 and a[cell_num] == 0:
        a[cell_num] = player

        if player == 1:
            x_start = (cell_num % 3) * 70 + 60
            y_start = (cell_num // 3) * 70 + 60
            cs.create_line(x_start, y_start, x_start + 50, y_start + 50, fill="red", width=5, tags="player_move")
            cs.create_line(x_start, y_start + 50, x_start + 50, y_start, fill="red", width=5, tags="player_move")
        elif player == 2:
            x_center = (cell_num % 3) * 70 + 85
            y_center = (cell_num // 3) * 70 + 85
            cs.create_oval(x_center - 20, y_center - 20, x_center + 20, y_center + 20, outline="blue", width=5, tags="player_move")

        c = 1 - c

        winner = check_win()
        if winner:
            show_game_over(winner)
        elif 0 not in a:
            show_game_over(0)

def click(event):
    draw_f(event.x, event.y, 1 if c == 0 else 2)

tk = Tk()
tk.title("Крестики-нолики")
tk.geometry("500x500")
tk.configure(bg="black")

cs = Canvas(tk, width=500, height=500, bg="black")
cs.pack()

cs.create_line(50, 120, 250, 120, fill="white")
cs.create_line(50, 180, 250, 180, fill="white")
cs.create_line(120, 50, 120, 250, fill="white")
cs.create_line(180, 50, 180, 250, fill="white")

a = [0] * 9
c = 0
game_over_label = None

tk.bind("<Button-1>", click)
tk.bind("<Return>", lambda event: reset_game())

tk.mainloop()
