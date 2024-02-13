import turtle

t = turtle.Turtle()
l = 100
f = 3
a = 360 / f
t.color('red', 'green')
t.hideturtle()

for _ in range(f):
    t.begin_fill()
    for _ in range(4):
        t.forward(l)
        t.left(90)
    t.end_fill()
    t.left(a)

t.penup()
turtle.done()

# square = turtle.Turtle()
# square.hideturtle()
# square.color('red')
# square.speed(10)
# square.begin_fill()
# for i in range(4):
#     square.forward(100)
#     square.right(90)
# square.end_fill()
# square.penup()
# square.done()