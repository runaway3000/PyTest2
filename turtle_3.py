import turtle

t = turtle.Turtle()
l = 100
a = 120
t.color('red')
t.hideturtle()
t.begin_fill()

for _ in range(3):
    t.forward(l)
    t.left(a)
t.end_fill()
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