import turtle

def polygon(sides, length):
  t = turtle.Turtle()
  t.color("lime")
  t.speed(0)
  angle = 360 / sides
  for side in range(sides):
    t.forward(length)
    t.right(angle)
  t.hideturtle()

for s in range(1):
    polygon(3, 35)
    polygon(4, 35)
    polygon(5, 35)
    polygon(6, 35)
    polygon(7, 35)
    polygon(8, 35)
    polygon(9, 35)
    polygon(10, 35)
    polygon(11, 35)
    polygon(12, 35)
  






