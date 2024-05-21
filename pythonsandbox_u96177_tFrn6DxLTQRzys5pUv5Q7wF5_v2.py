import turtle
import random

tj = turtle.Turtle()
tj.speed(5)
tj.pensize(2)
tj.shape("turtle")

for _ in range(150):  
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255) 
    tj.color(r, g, b)
    
    radius = random.randint(50, 150)
    
    tj.penup()
    areax = random.randint(-200, 200)
    areay = random.randint(-200, 200)
    
    tj.goto(areax, areay)
    tj.pendown()
    tj.circle(radius)

tj.hideturtle()
turtle.done()
