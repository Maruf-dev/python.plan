import turtle 
t=turtle.Turtle()
t.color("cyan")
t.width(3)
t.speed(0)
def kvadrat ():
    
    for n in range (4):
        t.forward(60)
        t.right(90)
kvadrat()
for v in range (73):
    kvadrat()
    t.forward(5)
    t.left(5)