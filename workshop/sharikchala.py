import turtle
t = turtle.Turtle()
# This code works!

def balloon(t, color):
    t.speed(0)
    t.color(color)

    # Draw balloon body.
    for side in range(30):
        t.forward(10)
        t.left(12)

    # Draw balloon knot.
    t.right(60)
    for side in range(3):
      t.forward(10)
      t.right(120)

    # Draw balloon string.
    t.color("gray")
    t.right(30)
    t.forward(100)




t.penup()
t.back(100)
t.pendown()
balloon(t, "red")

t.penup()
t.home()
t.pendown()
balloon(t, "blue")

t.penup()
t.home()
t.forward(100)
t.pendown()
balloon(t, "purple")

t.hideturtle()