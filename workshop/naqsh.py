import turtle
t = turtle.Turtle()
t.color("white")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return number * number

for n in range(540):
    angle = square(n)
    t.right(angle + .5)
    t.forward(5)