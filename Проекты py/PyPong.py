from tkinter import *
import random

tk = Tk()
tk.title("PyPong")

WIDTH = 900
HEIGHT = 300
PAD_W = 10
PAD_H = 100
BRADIUS = 25
SPEEDY = 0
SPEEDX = 10
PLAYER1 = 0
PLAYER2 = 0
INSPEED = 20
SPEED_MULTIPLY = 1.00
MAX_SPEED = 100
#score
def updatescr(player):
    global PLAYER1,PLAYER2
    if player == "right":
        PLAYER1+=1
        c.itemconfig(p1txt,text = PLAYER1)
    else:
        PLAYER1+=2
        c.itemconfig(p1txt,text = PLAYER2)
def respawn_ball():
    global SPEEDX
    canvas.coords(BALL,WIDTH / 2 - BRADIUS / 2,
                          HEIGHT / 2 - BRADIUS / 2,
                          WIDTH / 2 + BRADIUS / 2,
                          HEIGHT / 2 + BRADIUS / 2)
    SPEEDX =-(SPEEDX*INSPEED/abs(SPEEDX))

right_line_distance = WIDTH - PAD_W
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

canvas.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
canvas.create_line(WIDTH - PAD_W, 0, WIDTH - PAD_W, HEIGHT, fill="white")
canvas.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")

# Ball/paddles
BALL = canvas.create_oval(WIDTH / 2 - BRADIUS / 2,
                          HEIGHT / 2 - BRADIUS / 2,
                          WIDTH / 2 + BRADIUS / 2,
                          HEIGHT / 2 + BRADIUS / 2, fill="white")
LEFT_PAD = canvas.create_line(PAD_W, HEIGHT / 2 - PAD_H / 2, PAD_W, HEIGHT / 2 + PAD_H / 2, width=PAD_W, fill="white")
RIGHT_PAD = canvas.create_line(WIDTH - PAD_W, HEIGHT / 2 - PAD_H / 2, WIDTH - PAD_W, HEIGHT / 2 + PAD_H / 2, width=PAD_W, fill="white")
PSPEED = 10
LEFT_PSPEED = 0
RIGHT_PSPEED = 0
#points
p1txt = canvas.create_text(WIDTH - WIDTH/6,
                       PAD_H/4,text =PLAYER1,
                       font = "Arial 24",
                       fill = "white")
p2txt = canvas.create_text(WIDTH - WIDTH/6,
                       PAD_H/4,text =PLAYER2,
                       font = "Arial 24",
                       fill = "white")


# Collision
def collision(action):
    global SPEEDX, SPEEDY
    if action == "strike":
        SPEEDY = random.randrange(-15, 15)
        if abs(SPEEDX) < MAX_SPEED:
            SPEEDX = SPEEDX * 1.2 * SPEED_MULTIPLY
        else:
            SPEEDX = SPEEDX * SPEED_MULTIPLY 
    else: # ricochet
        SPEEDY = -SPEEDY

# Ball movement and boundary checks
def gravimove():
    global SPEEDX, SPEEDY
    ball_coords = canvas.coords(BALL)
    ball_left, ball_top, ball_right, ball_bottom = ball_coords
    ball_center_y = (ball_top + ball_bottom) / 2
    pad_left_top, pad_left_bottom = canvas.coords(LEFT_PAD)[1], canvas.coords(LEFT_PAD)[3]
    pad_right_top, pad_right_bottom = canvas.coords(RIGHT_PAD)[1], canvas.coords(RIGHT_PAD)[3]

    canvas.move(BALL, SPEEDX, SPEEDY)

    if ball_top + SPEEDY < 0 or ball_bottom + SPEEDY > HEIGHT:
        collision("ricochet")

    # Collision with left and right edges (paddles)
    if ball_right + SPEEDX > right_line_distance and SPEEDX > 0:
        if pad_right_top < ball_center_y < pad_right_bottom:
            collision("strike")
            SPEEDX = -abs(SPEEDX) # Reverse direction
        else:
            collision("ricochet")
            SPEEDX = -abs(SPEEDX) # Reverse direction
    elif ball_left + SPEEDX < PAD_W and SPEEDX < 0: 
        if pad_left_top < ball_center_y < pad_left_bottom:
            collision("strike")
            SPEEDX = abs(SPEEDX) # Reverse direction
        else:
            collision("ricochet")
            SPEEDX = abs(SPEEDX) # Reverse direction

# Paddle movement
def move_pads():
    global LEFT_PSPEED, RIGHT_PSPEED
    canvas.move(LEFT_PAD, 0, LEFT_PSPEED)
    if canvas.coords(LEFT_PAD)[1] < 0:
        canvas.move(LEFT_PAD, 0, -canvas.coords(LEFT_PAD)[1])
    elif canvas.coords(LEFT_PAD)[3] > HEIGHT:
        canvas.move(LEFT_PAD, 0, HEIGHT - canvas.coords(LEFT_PAD)[3])
    canvas.move(RIGHT_PAD, 0, RIGHT_PSPEED)
    if canvas.coords(RIGHT_PAD)[1] < 0:
        canvas.move(RIGHT_PAD, 0, -canvas.coords(RIGHT_PAD)[1])
    elif canvas.coords(RIGHT_PAD)[3] > HEIGHT:
        canvas.move(RIGHT_PAD, 0, HEIGHT - canvas.coords(RIGHT_PAD)[3])

# Main game loop
def main():
    gravimove()
    move_pads()
    tk.after(30, main)

canvas.focus_set()
# Key press event handler
def contrmove(event):
    global LEFT_PSPEED, RIGHT_PSPEED
    if event.keysym == "w":
        LEFT_PSPEED = -PSPEED
    elif event.keysym == "s":
        LEFT_PSPEED = PSPEED
    elif event.keysym == "Up":
        RIGHT_PSPEED = -PSPEED
    elif event.keysym == "Down":
        RIGHT_PSPEED = PSPEED

canvas.bind("<KeyPress>", contrmove)

# Key release event handler
def stop_pad(event):
    global LEFT_PSPEED, RIGHT_PSPEED
    if event.keysym in "ws":
        LEFT_PSPEED = 0
    if event.keysym in ("Up", "Down"):
        RIGHT_PSPEED = 0

canvas.bind("<KeyRelease>", stop_pad)

# Start the game
main()
tk.mainloop()
