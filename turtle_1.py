import turtle

t = turtle.Turtle()
t.color("red")
t.width(2)
t.speed(0.5)

a = 300
b = 30
shag = a / b

for _ in range(b):
    for _ in range(4):
        t.forward(a)
        t.left(90)
    a -= shag

turtle.done()