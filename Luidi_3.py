from turtle import *
#import turtle
import math

luis=Turtle()
luis.shape("turtle")
luis.speed(10)

def polygon(t, n, length):
    for i in range(n):
        left(360/n)
        forward(length)

def draw_circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
    exitonclick()

draw_circle(luis, 30)
draw_circle(luis, 50)
draw_circle(luis, 70)
