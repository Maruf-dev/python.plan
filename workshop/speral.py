import turtle

lengths = [5,10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,120,130,140,150,160,170]

dizzy = turtle.Turtle()
dizzy.color("blue")
dizzy.width(5)

for lengths in lengths:
    dizzy.forward(lengths)
    dizzy.right(90)
