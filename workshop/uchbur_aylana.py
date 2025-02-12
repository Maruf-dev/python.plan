import turtle


def tri(color, start):
    t=turtle.Turtle()
    t.speed(0)
    t.width(3)
    t.color(color)
    t.right(start)
    
    for shape in range(6):
        t.right(15)
        for side in range(3):
            t.forward(100)
            t.right(120)
tri("red", 0)
tri("orange", 120)
tri("blue",240)
# Write a function here that creates a
# turtle and draws a shape with it.



# Call the function multiple times.

