import turtle as t


t.shape("turtle")
t.pensize(20)
t.speed(0)

t.circle(100)

t.penup()
t.forward(240)
t.pendown()
t.pencolor("red")
t.circle(100)

t.penup()
t.back(480)
t.pendown()
t.pencolor("blue")
t.circle(100)

t.penup()
t.forward(120)
t.goto(-120,-120)
t.pendown()
t.pencolor("yellow")
t.circle(100)

t.penup()
t.forward(240)
t.pendown()
t.pencolor("green")
t.circle(100)



t.done()