# python 2

# You can edit this code and run it right here in the browser!
# Try changing colors or adding your own shapes.
import math
import turtle


def draw_circle(turtle, color, size, x, y):

    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(10)

draw_circle(tommy, "green", 10, 25, 0)
draw_circle(tommy, "blue", 20, 0, 0)
draw_circle(tommy, "yellow", 30, -25, 0)


tommy.penup()
tommy.goto(0,-50)
tommy.color("black")
tommy.write("Teach With Code!")
tommy.goto(0,-80)


turtle.exitonclick()