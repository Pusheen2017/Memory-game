import turtle

# --- ekran ---
screen = turtle.Screen()
screen.title("Żółwiowy paint")
screen.bgcolor("lightblue")

# --- żółw ---
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.pensize(3)
t.speed(0)

STEP = 20

# --- ruch ---
def up():
    t.setheading(90)
    t.forward(STEP)

def down():
    t.setheading(270)
    t.forward(STEP)

def left():
    t.setheading(180)
    t.forward(STEP)

def right():
    t.setheading(0)
    t.forward(STEP)

# --- kolory ---
colors = ["green", "red", "blue", "purple", "orange", "black", "yellow"]
color_index = 0

def color_next():
    global color_index
    color_index = (color_index + 1) % len(colors)
    t.color(colors[color_index])

def color_prev():
    global color_index
    color_index = (color_index - 1) % len(colors)
    t.color(colors[color_index])

# --- pisak ---
def pen_up():
    t.penup()

def pen_down():
    t.pendown()

# --- klawisze ---
screen.listen()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.onkey(color_prev, "a")
screen.onkey(color_next, "d")

screen.onkey(pen_up, "space")
screen.onkey(pen_down, "Shift_L")   # lewy Shift
screen.onkey(pen_down, "Shift_R")   # prawy Shift

# --- start ---
screen.mainloop()
