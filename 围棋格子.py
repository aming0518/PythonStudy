import turtle



turtle.showturtle()
step=20
for i in range(10):
    turtle.penup()
    turtle.goto(0,step*i)
    turtle.pendown()
    turtle.forward(step*10)


turtle.right(270)
for i in range(10):
    turtle.penup()
    turtle.goto(step*i,0)
    turtle.pendown()
    turtle.forward(step*10)


turtle.dot(10,"black")

turtle.done()
