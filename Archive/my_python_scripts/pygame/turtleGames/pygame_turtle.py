from turtle import *
from colorsys import *

setup(width=800, height=800)
speed(0)
bgcolor('black')
pensize(2)
tracer(10)
h = 0
for i in range(150):
    c = hsv_to_rgb(i/150 ,1,1)
    color(c)
    rt(4)
    circle(40, 4)
    lt(90)
    circle(40,10)
    lt(90)
    circle(40,10)
    lt(180)


hideturtle()
done()