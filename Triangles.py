import turtle
def t(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+100,y)
    turtle.goto(x+50,y-100)
    turtle.goto(x,y)
        
