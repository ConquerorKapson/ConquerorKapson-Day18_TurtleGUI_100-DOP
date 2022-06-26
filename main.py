import random
import turtle as t
import colorgram

colors = colorgram.extract("hirst_spot_painting.jpg", 15)

kachua = t.Turtle()
screen = t.Screen()
t.colormode(255)
kachua.turtlesize(2)
kachua.shape("turtle")
kachua.speed("fastest")

color = []


def color_selection():
    for val in colors:
        r = val.rgb.r
        g = val.rgb.g
        b = val.rgb.b
        val = (r, g, b)
        color.append(val)


color_selection()

color_list = [
    (199, 175, 117),
    (124, 36, 24),
    (210, 221, 213),
    (168, 106, 57),
    (186, 158, 53),
    (6, 57, 83),
    (109, 67, 85),
    (113, 161, 175),
    (22, 122, 174),
    (64, 153, 138),
    (39, 36, 36),
    (76, 40, 48)
]

gap = 70
start = -310

for i in range(10):
    if i % 2 == 0:
        kachua.showturtle()
    else:
        kachua.hideturtle()
    kachua.penup()
    kachua.setx(start)
    kachua.sety(start + gap * i)
    for j in range(10):
        col = random.choice(color_list)
        kachua.dot(30, col)
        kachua.forward(gap)
screen.exitonclick()
