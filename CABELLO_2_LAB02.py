import turtle
import random

tj = turtle.Turtle()
tj.speed(5)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
tj.pensize(2)
tj.shape("turtle")

for _ in range(150):  
    tj.color(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255) 
    tj.color(r, g, b)
    tj.circle(100)


    radius = random.randint(50, 150)
    tj.circle(radius)
    tj.left(50)
    
tj.hideturtle()
turtle.done()