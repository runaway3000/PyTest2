import turtle
import math

circle = turtle.Turtle()

lists = 20
R = 100

lists_a = 360 / lists
circle.speed(5)
circle.goto(0, -R)
circle.shape(None)
circle.begin_fill()
circle.color("orange")
circle.circle(R)
circle.end_fill()

def drow_list(x, y, a):
    list = turtle.Turtle()
    list.color('red', 'green')
    list.hideturtle()

    list.penup()
    list.setpos(x, y)
    list.seth(0)
    list.speed(1)
#    list.seth(a)
#    list.left(19)
    list.begin_fill()
    list.pendown()

    r = math.sqrt(x ** 2 + y ** 2)

    theta = math.atan2(y, x)
    print(f"lists_a = {lists_a}, i = {i} x = {x}, y = {y}, Угол = {math.degrees(theta)}")

    list.left(math.degrees(theta))

    list.right(20)
    for _ in range(40):
        list.forward(5)
        list.left(1)

    list.left(140)
    for _ in range(40):
        list.forward(5)
        list.left(1)

    list.end_fill()
    list.penup()

for i in range(lists):
    x = math.sin(math.radians(lists_a * i)) * R
    y = math.cos(math.radians(lists_a * i)) * R
    drow_list(x, y, lists_a * (i - 1))

turtle.done()