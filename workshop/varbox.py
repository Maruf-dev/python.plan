import turtle
xay = turtle.Turtle()

xay.width(5)

for side in ["red","orange","blue"] :
    xay.color(side)    
    xay.penup()
    xay.forward(65)
    xay.pendown()



    for man in [50,50,50,50]:
       xay.forward(man)
       xay.right(90)
      



     