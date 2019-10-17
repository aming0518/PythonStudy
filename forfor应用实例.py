import turtle

for  i in range(0,300,100):
    for j in range(0,400,100):

        turtle.goto(i,j)
        turtle.pendown()
        turtle.write(str(i)+","+str(j))
    turtle.penup()




turtle.done()