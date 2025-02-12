import random
mood =random.choice([ "sad", "happy", "angry", "party"])

import turtle
riley = turtle.Turtle()
riley.width(5)

# Add your code here.
if mood == "happy":
    riley.color("yellow")
elif mood == "sad" :
        riley.color("blue")
elif mood == "angry" :
        riley.color("green") 
elif mood == "party":
        riley.color("red")
for side in range(5):
    riley.forward(100)
    riley.right(144)