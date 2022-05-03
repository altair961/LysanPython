import turtle
x=int(input())
y=int(input())
turtle.penup()
turtle.goto(x,y+100)
turtle.pendown()
turtle.goto(x+100,y+100)
turtle.goto(x,y)
turtle.goto(x,y+100)
