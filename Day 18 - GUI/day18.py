# @author   Lucas Cardoso de Medeiros
# @since    25/06/2022
# @version  1.0

# Turtle GUI

import turtle as t
import random
import colorgram

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_square(turtle, shape, color):
    turtle.shape(shape)
    turtle.color(color)
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line(turtle, shape, color, size):
    turtle.shape(shape)
    turtle.color(color)
    x = -0
    y = 0
    turtle.setpos(x, y)
    for line in range(10):
        for i in range(size):
            turtle.pendown()
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
        y -= 20
        turtle.up()
        turtle.setpos(x, y)


def draw_shapes(turtle, shape, num):
    turtle.shape(shape)
    for num_faces in range(3, num):
        turtle.color(random_color())
        for side in range(num_faces):
            turtle.forward(100)
            turtle.right(360 / num_faces)


def random_walk(turtle, shape, length):
    turtle.pensize(10)
    turtle.shape(shape)
    turtle.speed("fast")
    for i in range(length):
        turtle.color(random_color())
        turtle.setheading(random.choice(directions))
        turtle.fd(30)


def draw_circles(turtle, shape, num):
    turtle.shape(shape)
    turtle.speed("fastest")
    angle = 0
    for i in range(num):
        turtle.setheading(angle)
        turtle.color(random_color())
        turtle.circle(100)
        angle -= (360 / num)


def get_colors():
    color_list = []
    colors = colorgram.extract('image.jpg', 84)
    for color in colors:
        color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return color_list


def paint(turtle, lines, columns, size):
    y = 0
    x = -400
    colors = get_colors()
    turtle.hideturtle()
    turtle.speed("fast")
    turtle.up()
    turtle.setpos(x, y)
    for line in range(lines):
        for i in range(columns):
            turtle.dot(size, random.choice(colors))
            turtle.fd(size * 2)
        y += size * 2
        turtle.up()
        turtle.setpos(x, y)


if __name__ == '__main__':
    timmy = t.Turtle()
    t.colormode(255)
    paint(timmy, 10, 10, 20)
    screen = t.Screen()
    screen.exitonclick()
