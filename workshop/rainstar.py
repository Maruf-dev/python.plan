import turtle
xay = turtle.Turtle()
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
xay.width(5)
for side in rainbow :
    xay.color(side)

    for big in [1,1,1,1,1,]:
        xay.forward(60)
        xay.right(144)
    
    xay.right(60)
    xay.penup()
    xay.forward(50)
    xay.pendown()