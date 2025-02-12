import turtle
xay = turtle.Turtle()

xay.width(5)
xay.speed(1)

for man in ["orange", "red","blue"] :
    xay.color(man)
    xay.forward(50)
    xay.penup()
    xay.forward(20)
    xay.pendown()