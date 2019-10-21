import turtle



turtle.showturtle()

turtle.pensize(10)
step=20
for i in range(8):
    for j in range(8):
        turtle.penup()
        turtle.goto(i*step,j*step)
        turtle.pendown()

        turtle.begin_fill()
        if (i+j)%2==0:
            turtle.color("black")
        else:
            turtle.color("white")
        for k in range(4):
            turtle.forward(step)
            turtle.right(90)
        turtle.end_fill()

turtle.done()
