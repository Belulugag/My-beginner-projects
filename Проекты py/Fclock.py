from tkinter import *
import math
import time

tk = Tk()
tk.geometry("450x450")
tk.title("Fclock")
tk.resizable(False, False)
height = 400
width = 400
r = 180
cs = Canvas(tk, width=width, height=height, bg="white")
cs.pack(padx=25, pady=25)
def x_coords(length, angle):
    return width / 2 + length * math.cos(angle * math.pi / 180)
def y_coords(length, angle):
    return height / 2 + length * math.sin(angle * math.pi / 180)
cs.create_oval(width / 2 - r, height / 2 - r, width / 2 + r, height / 2 + r, outline="black", width=2)
for i in range(1, 13):
    angle = (i - 3) * 30
    x_mark = x_coords(r, angle)
    y_mark = y_coords(r, angle)
    cs.create_text(x_coords(r - 20, angle), y_coords(r - 20, angle), text=str(i), font=("Arial", 14))
    x_inner_mark_short = x_coords(r - 10, angle)
    y_inner_mark_short = y_coords(r - 10, angle)
    cs.create_line(x_mark, y_mark, x_inner_mark_short, y_inner_mark_short, width=2)
for i in range(0, 60, 5):
    angle = (i - 15) * 6
    x_mark = x_coords(r, angle)
    y_mark = y_coords(r, angle)
    x_inner_mark_long = x_coords(r - 15, angle)
    y_inner_mark_long = y_coords(r - 15, angle)
    cs.create_line(x_mark, y_mark, x_inner_mark_long, y_inner_mark_long, width=3)

hour_hand = None
minute_hand = None
second_hand = None

def update_clock():
    global hour_hand, minute_hand, second_hand
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec
    hour_angle = (hour + minute / 60) * 30 - 90
    minute_angle = minute * 6 - 90
    second_angle = second * 6 - 90
    if hour_hand:
        cs.delete(hour_hand)
    if minute_hand:
        cs.delete(minute_hand)
    if second_hand:
        cs.delete(second_hand)
    x1_h = x_coords(r * 0.5, hour_angle)
    y1_h = y_coords(r * 0.5, hour_angle)
    hour_hand = cs.create_line(width / 2, height / 2, x1_h, y1_h, fill="black", width=8)
    x1_m = x_coords(r * 0.75, minute_angle)
    y1_m = y_coords(r * 0.75, minute_angle)
    minute_hand = cs.create_line(width / 2, height / 2, x1_m, y1_m, fill="blue", width=5)
    x1_s = x_coords(r * 0.85, second_angle)
    y1_s = y_coords(r * 0.85, second_angle)
    second_hand = cs.create_line(width / 2, height / 2, x1_s, y1_s, fill="red", width=2)
    tk.after(1000, update_clock)
update_clock()
tk.mainloop()
