from turtle import Turtle, Screen
import random
import heroes

kachua = Turtle()
screen = Screen()
kachua.shape("classic")
kachua.speed("slow")
no_of_sides = [3, 4, 5, 6, 7, 8, 9, 10, 12, 15]
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

for val in no_of_sides:
    angle = 360 / val
    kachua.pencolor(random.choice(colors))
    kachua.penup()
    kachua.setx(-50)
    kachua.sety(200)
    kachua.pendown()
    for i in range(val):
        kachua.forward(100)
        kachua.right(angle)

screen.exitonclick()
