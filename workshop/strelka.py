import turtle
xay = turtle.Turtle()
xay.color("red")
xay.width(5)
angles = [-90, 0, 0, -90,
          135, 0, 0, 0, 
          90, 0, 0, 0,
          135, -90, 0, 0,
          90, 0, 0, 0]
for angle in angles :
   xay.right(angle)
   xay.forward(25)          