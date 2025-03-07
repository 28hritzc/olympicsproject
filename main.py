import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('tan')
t = turtle.Turtle()
t.speed(0)


t.penup()
t.goto(-155,125)
t.pendown()
t.pencolor('blue')
t.pensize(5)
t.fillcolor()
t.begin_fill()
t.circle(50)

t.penup()
t.goto(-40,125)
t.pendown()
t.pencolor('black')
t.pensize(5)
t.fillcolor()
t.begin_fill()
t.circle(50)

t.penup()
t.goto(80,125)
t.pendown()
t.pencolor('red')
t.pensize(5)
t.fillcolor()
t.begin_fill()
t.circle(50)

t.penup()
t.goto(-100,60)
t.pendown()
t.pencolor('yellow')
t.pensize(5)
t.fillcolor()
t.begin_fill()
t.circle(50)

t.penup()
t.goto(20,60)
t.pendown()
t.pencolor('green')
t.pensize(5)
t.fillcolor()
t.begin_fill()
t.circle(50)

t.penup()
t.goto(-30,250)
t.pendown()
t.pencolor('purple')
t.write("Winter Olympics",font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(-35,0)
t.pendown()
t.pencolor('purple')
t.write("2026",font=("Arial",30,"bold"),align="center")

#blue, yellow, black, green, and red

turtle.done()