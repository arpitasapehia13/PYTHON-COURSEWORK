import turtle
turtle.showturtle()
turtle.left(90)
turtle.goto(0, -50)
turtle.forward(100)
turtle.backward(100)
turtle.backward(100)
turtle.right(90)
turtle.penup()
turtle.pendown()
turtle.right(100)
turtle.forward(100)
turtle.goto(0, -100)
turtle.centre(45)
Traceback(most recent call last):
    File "<pyshell#13>", line 1, in <module >
    turtle.centre(45)
AttributeError: module 'turtle' has no attribute 'centre'
turtle.circle(45)
turtle.bgcolor("pink")
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(45)
turtle.end_fill()
