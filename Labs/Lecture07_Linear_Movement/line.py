import turtle
import random
import math


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(1, 1, 1)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, 0, 0, 0)


def draw_line_basic(p1, p2):
    # fill here
    pass


def draw_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        draw_point((x, y))
    draw_point(p2)

def draw_circle():

    t = 0.0

    r = 200
    while t <= 2 * math.pi:
        x = r * math.cos(t)
        y = r * math.sin(t)
        t += (math.pi/ 10)
        draw_point((x,y))


def draw_shape():

    a = 170
    b = 100
    t = 0.0

    while t <= 20 * math.pi:
        x = (a-b)*math.cos(t) + b*math.cos(t*(a/b-1))
        y = (a-b)*math.sin(t) - b*math.sin(t*(a/b-1))
        t += (math.pi / 30)
        draw_point((x, y))

prepare_turtle_canvas()

#draw_line((-100,50),(100,50))
draw_shape()

turtle.done()