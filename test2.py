import turtle as t
import random

kachua = t.Turtle()
screen = t.Screen()

kachua.speed("fastest")
angle = 360
tilt = 8
iteration = int(angle/tilt)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]

while True:
    val = random.choice(colors)
    kachua.fillcolor(val)
    kachua.begin_fill()
    kachua.pencolor(val)
    kachua.circle(200)
    # kachua.forward(5)
    kachua.left(8)
    kachua.end_fill()
    # iteration -= 1

screen.exitonclick()
