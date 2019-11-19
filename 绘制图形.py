import turtle
turtle.screensize(1024,768)#屏幕大小

turtle.write("hello天朝",font=("",80,"normal"))
turtle.showturtle()   #展示

turtle.begin_fill()#开始填充
turtle.circle(200,steps=5) #用圆花图形  几边形就steps=几
turtle.color("blue")#填充颜色
turtle.end_fill()#结束填充

turtle.done()