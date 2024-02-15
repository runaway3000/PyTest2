import turtle
t = turtle.Turtle()


cont_r = int(input("Введите количество кругов: "))
rad_r = int(input("Введите радиус кругов: "))

vers_t = []

deg_t = 360 / cont_r

def get_pos(a, vers_t):
    a = t.position()
    vers_t.append(a)
t.penup()
for _ in range(cont_r):
    get_pos(t.position(), vers_t)
    t.forward(rad_r*2)
    t.left(deg_t)
t.pendown()

for i in list(vers_t):
    t.penup()
    t.goto(i)
    t.forward(rad_r)
    t.pendown()
    t.circle(rad_r)
    print(i)

turtle.done()