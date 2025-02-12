import turtle
import random

t=turtle.Turtle()
t.width(10)
t.speed(3)
colors=["red","black","blue","orange","lime","yellow","brown","green","purple"]

def spur():

    for step in range(100):
        tt= random.choice(colors)
        tx = random.randint(-90,90)
        t.color(tt)
        
        t.right(tx)
        t.forward(10)
spur()