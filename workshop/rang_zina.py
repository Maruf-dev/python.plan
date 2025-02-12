import turtle 
t = turtle.Turtle()
def kvad () :
    for side in range(5) :
        if side == 1 :
           t.color("blue")
        else:
            t.color("red") 
            t.width(4)  
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.right(90)

     
kvad() 