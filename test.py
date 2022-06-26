import turtle as t
import random

kachua = t.Turtle()
screen = t.Screen()

length = 30
kachua.pensize(10)
kachua.speed("slow")
iteration = 200
directions = [0, 90, 180, 270]
t.colormode(255)


# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


while True:
    kachua.pencolor(random_color())
    kachua.forward(length)
    kachua.setheading(random.choice(directions))
    # iteration -= 1

screen.exitonclick()
