import turtle
import colorgram
import random
from turtle import Turtle,Screen

colors=colorgram.extract('sweet_pic.jpg',15)
print(colors)

renkler=[(254, 253, 253), (101, 190, 171), (100, 164, 209), (207, 137, 182),
         (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211), (25, 26, 26),
         (217, 163, 85), (254, 253, 253), (101, 190, 171), (100, 164, 209),
         (207, 137, 182), (213, 230, 240), (56, 179, 154), (49, 124, 170),
         (187, 222, 211), (25, 26, 26), (217, 163, 85), (239, 212, 97), (189, 89, 132),
         (124, 73, 114), (160, 209, 185), (89, 126, 186)]

t=Turtle()
t.hideturtle()
screen=Screen()
t.pensize(width=8)
t.penup()
screen.colormode(255)
t.speed(0)
t.goto(-150,-150)
m=4
for i in range(8):
    for j in range(8):
        t.pendown()
        t.pensize(width=2)
        t.pencolor("black")  # Çerçeve rengi
        t.fillcolor(random.choice(renkler))  # Doldurma rengi
        t.begin_fill()
        for _ in range(4):
            t.forward(30)
            t.right(90)
        t.end_fill()
        t.penup()
        # t.dot(22,"black")
        # t.dot(22)
        # t.dot(random.choice(renkler))
        t.forward(40)  # Bir sonraki sütuna git
    t.backward(40 * 8)
    t.setheading(90)
    t.forward(40)
    t.setheading(0)
screen.exitonclick()


