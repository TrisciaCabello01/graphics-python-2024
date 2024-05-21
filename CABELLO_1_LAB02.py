import turtle
tj = turtle.Turtle()
tj.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
tj.shape("turtle")
tj.pensize(10)

# rectangle fill
tj.color("green","orange")
tj.penup()
tj.goto(-60,180)
tj.pendown()
tj.begin_fill()
tj.forward(100)
tj.right(90)
tj.forward(100)
tj.right(90)
tj.forward(100)
tj.right(90)
tj.forward(100)
tj.end_fill()

#triangle fill
tj.color("blue", "violet")
tj.penup()
tj.goto(-60,0)
tj.right(180)
tj.forward(50)
tj.pendown()
tj.begin_fill()
tj.left(90)
tj.forward(100)
tj.left(120)
tj.forward(100)
tj.left(120)
tj.forward(100)
tj.end_fill()

#circle fill
tj.color("red", "yellow")
tj.penup()
tj.goto(-50, -120)
tj.pendown()
tj.begin_fill()
tj.circle(50)
tj.end_fill()

