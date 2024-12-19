import turtle
import random
from turtle import Turtle,Screen
import colorgram

colors=colorgram.extract('sweet_pic.jpg',10)
print(colors)
renkler=[(254, 253, 253), (101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211), (25, 26, 26), (217, 163, 85)]
# for i in range(len(colors)):
#     color=colors[i]
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#
#     renkler.append((r,g,b))
# print(renkler)
screen=Screen()
t=Turtle()
t.hideturtle()
t.penup()
screen.colormode(255)
t.speed(0)
t.pensize(width=10)
t.goto(-200,-200)
for i in range (8):
    for j in range(8):
        t.dot(25, "black")
        t.dot(10)
        t.dot(random.choice(renkler))
        t.forward(40)  # Bir sonraki sütuna git

    t.backward(40 * 8)  # Satırın başına dön
    t.setheading(90)  # Bir satır yukarı çık
    t.forward(40)
    t.setheading(0)  # Yine sağa gitmek için yönü sıfırla

    #     if t.xcor()<=199 and t.heading()==0:
    #         t.forward(40)
    # t.setheading(90)
    # t.forward(40)
    # t.setheading(180)
    # t.forward(200)
screen.exitonclick()


    # seni seviyorum ♥